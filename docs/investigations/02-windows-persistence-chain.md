# Investigation 02 — New Account and Scheduled Task

<badge>Illustrative case study · synthetic telemetry</badge>

## Case summary

**Case ID:** LAB-IR-002  
**Severity:** High (proposed)  
**Disposition:** Escalate for endpoint and change-control validation  
**Host:** `LAB-WIN-07`  
**User context:** `SYSTEM` and a newly created local account `svc_update2`

## Evidence timeline

| Time (UTC) | Telemetry | Synthetic observation |
|---|---|---|
| 09:14 | Security Event 4720 | Local account `svc_update2` created |
| 09:16 | Security Event 4732 | New account added to local Administrators group |
| 09:20 | Security Event 4698 | Scheduled task `UpdateTelemetryCache` created |
| 09:20 | Sysmon Event 1 | `schtasks.exe` launched with `/Create` |
| 09:21 | Sysmon Event 1 | Task action references a script under a user-writable path |

These records are synthetic examples; they are not exports from an actual Windows endpoint.

## Detection result

**Triggered rules:** `ST-DET-02`, `ST-DET-04`  
**ATT&CK mapping:** T1136.001 (Local Account), T1053.005 (Scheduled Task)

**Illustrative SIEM output:**

```text
[HIGH] ST-DET-02  Account created: svc_update2
[HIGH] ST-DET-04  Scheduled task created: UpdateTelemetryCache
Host: LAB-WIN-07
Change ticket: not supplied in lab scenario
Triage status: ESCALATE
```

## Analyst assessment

A new local account, privileged-group membership, and task creation in a short period form a higher-risk sequence than any one event alone. However, device provisioning or an approved application installer may create similar artifacts.

## L1 checklist

1. Identify the account creator and verify the administrator identity.
2. Check whether the account was approved and whether it has interactive or remote logon rights.
3. Review group membership and first logon.
4. Obtain the scheduled task XML and inspect the action, trigger, run-as account, and executable path as text.
5. Check software inventory, deployment logs, and change tickets.
6. Escalate unexplained privileged account creation or suspicious task actions.

## Escalation note

> A local account was created and added to a privileged group shortly before a scheduled task was registered. The task action references a user-writable path. Validate the account creator, software deployment history, and task XML. No containment action has been taken in this training scenario.

## What I would improve

I would correlate account creation, group membership, scheduled-task registration, and first logon into one incident to reduce duplicate alerts and expose the sequence.
