# SentinelTrace Detection Engineering Pack

**Scope:** L1 monitoring and triage. The rules below are starting points, not universal production rules. Validate required telemetry, field mappings, thresholds, and exclusions in the target environment.

## Detection coverage

| ID | Use case | Main data source | Windows/Linux evidence | ATT&CK | Default severity |
|---|---|---|---|---|---|
| ST-DET-01 | Repeated authentication failures followed by success | Linux auth / Windows Security | SSH auth.log; Security 4625 then 4624 | T1110.001 | High / Critical on success |
| ST-DET-02 | New local account creation | Windows Security | 4720; optionally 4732/4728 for group addition | T1136.001 | High |
| ST-DET-03 | Encoded PowerShell execution | Sysmon / PowerShell Operational | Sysmon 1; PowerShell 4104; optionally Security 4688 | T1059.001 | High |
| ST-DET-04 | Suspicious scheduled task creation | Windows Security / Sysmon | 4698; Sysmon 1 with schtasks.exe /Create | T1053.005 | Medium / High with suspicious task action |
| ST-DET-05 | Unusual process access to LSASS | Sysmon | Sysmon 10 with TargetImage ending in lsass.exe | T1003.001 | High |

## ST-DET-01 — Authentication burst followed by success

**Hypothesis:** A single source producing multiple failed logons in a short period, followed by a successful logon, may indicate password guessing that obtained valid access.

**Minimum telemetry:** Linux OpenSSH authentication logs or Windows Security events 4625 and 4624. Preserve timestamp, source address, account, host, and status.

**Example threshold:** At least 5 failures from one source within 5 minutes; a success from that source within 10 minutes of the burst is a higher-priority correlated signal.

**Splunk:** See `splunk/01_auth_burst_success.spl`.

**Sentinel:** See `kql/01_auth_burst_success.kql`.

**Sigma:** See `sigma/windows_auth_burst.yml` (Windows 4625 event rule; the correlation step is expressed separately in SPL/KQL).

**False positives:** Vulnerability scanners, misconfigured service accounts, stale saved credentials, VPN/NAT egress shared by many users, password manager retries, scheduled jobs.

**Tuning:** Group by source and account where reliable; add approved scanner ranges and service-account context; avoid broad allowlists that hide a compromised source; compare against normal baseline by host and business hours.

**L1 triage:** Confirm source, targeted account(s), destination host, failure count, success status, MFA result if available, account owner, recent password reset, and nearby process/session activity. Escalate a success-after-failure sequence as potential account compromise; do not disable accounts or block IPs without the approved process.

## ST-DET-02 — New local account creation

**Hypothesis:** An unexpected local account creation, especially outside an approved change window or followed by privileged-group membership, may indicate persistence or unauthorized administration.

**Minimum telemetry:** Windows Security 4720 (user account created); enrich with 4732 (member added to local security-enabled group) or 4728 (member added to global security-enabled group), if collected.

**Splunk / Sentinel:** See `splunk/02_new_local_account.spl` and `kql/02_new_local_account.kql`.

**Sigma:** See `sigma/windows_new_local_account.yml`.

**False positives:** Approved endpoint provisioning, service installation, software deployment, help-desk activity, golden-image preparation.

**Tuning:** Maintain a change-ticket and approved-admin context source; baseline accounts created by device-management tooling; alert more strongly when the actor is unusual, the account is enabled for remote access, or the account is added to an admin group.

**L1 triage:** Identify the host, new account, actor/subject account, timestamp, group changes, logon activity after creation, asset owner, and linked change request. Escalate unexplained privileged-account creation.

## ST-DET-03 — Encoded PowerShell command

**Hypothesis:** PowerShell launched with encoded-command options can conceal command content. Encoding is not inherently malicious; correlate the parent process, user, script block, destination, signer, and change context.

**Minimum telemetry:** Sysmon Event ID 1 (Process Create), PowerShell Operational 4104 (script block logging), or Security 4688 with command-line auditing enabled.

**Splunk / Sentinel:** See `splunk/03_encoded_powershell.spl` and `kql/03_encoded_powershell.kql`.

**Sigma:** See `sigma/windows_encoded_powershell.yml`.

**False positives:** Software deployment tools, management agents, legitimate automation, configuration-management scripts, signed admin scripts.

**Tuning:** Exclude only verified automation paths and identities; preserve command-line and parent-process context; raise severity where the parent is an office application, script host, browser, or an unusual user-writable location.

**L1 triage:** Capture the full command line, parent process, user, host, process hash, script-block content if available, network connections, and change ticket. Do not execute the command to inspect it. Escalate suspicious chains for endpoint review.

## ST-DET-04 — Scheduled task creation

**Hypothesis:** A newly created scheduled task with an unusual action, user-writable path, encoded script, or unexpected run-as account may represent persistence.

**Minimum telemetry:** Security 4698 for scheduled task creation; Sysmon 1 for the process that invokes `schtasks.exe /Create`; task XML or EDR context is useful enrichment.

**Splunk / Sentinel:** See `splunk/04_scheduled_task_creation.spl` and `kql/04_scheduled_task_creation.kql`.

**Sigma:** See `sigma/windows_scheduled_task_creation.yml`.

**False positives:** Software updaters, backup agents, enterprise management, legitimate maintenance, browser updaters.

**Tuning:** Compare task name, author, action path, trigger, run-as account, parent process, and approved software inventory. Do not suppress all tasks created by SYSTEM; verify the task action.

**L1 triage:** Retrieve task name and XML, executable/script path, arguments, trigger, run-as account, creator, host criticality, and change ticket. Treat suspicious task action plus encoded PowerShell as higher priority.

## ST-DET-05 — Unusual access to LSASS

**Hypothesis:** A process accessing the LSASS process may be inspecting sensitive authentication memory. Sysmon Event ID 10 can supply source and target process context; a process-access event alone is not proof of credential dumping.

**Minimum telemetry:** Sysmon Event ID 10 (Process Access), with `TargetImage` identifying `lsass.exe`. EDR telemetry can add signer, hash, and protection status.

**Splunk / Sentinel:** See `splunk/05_lsass_process_access.spl` and `kql/05_lsass_process_access.kql`.

**Sigma:** See `sigma/windows_lsass_access.yml`.

**False positives:** EDR/AV agents, approved security tools, diagnostic tools, system components.

**Tuning:** Maintain a tightly controlled allowlist of verified security product binaries and signatures. Alert on unsigned or uncommon source processes, unusual users, and access outside expected maintenance windows.

**L1 triage:** Record source image, hash, signer, source user, target image, granted access, host, and nearby process/network events. Preserve evidence and escalate promptly; do not attempt to dump or inspect credential memory.

## Common operational checks

1. Confirm the exact event source and field mapping before enabling a rule.
2. Validate time synchronization and event completeness.
3. Run positive and negative test cases in an authorized isolated lab.
4. Record the query version, data source, threshold, exclusions, test date, and analyst owner.
5. Revisit thresholds after observing normal baseline volume.
6. Keep alerting separate from automated containment.
