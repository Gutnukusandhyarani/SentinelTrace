# Playbook — Suspicious Script, Scheduled Task, or Process Access

**Triggers:** Encoded PowerShell, unusual scheduled task creation, suspicious process access to LSASS, or correlated endpoint detections.

## 1. Validate telemetry

- Confirm host, timestamp, user, image, parent image, command line, signer, hash, and event source.
- Check that Sysmon/Windows Security/PowerShell telemetry is complete.
- For LSASS access, capture source process and access metadata; do not attempt to access or dump credential memory.

## 2. Add context

- Check approved software deployment, endpoint-management activity, task inventory, and change records.
- Correlate surrounding process, network, logon, and file events.
- Determine whether the event is isolated or part of a sequence.

## 3. Escalate

- Escalate suspicious unsigned scripts, unexpected task actions, unusual parent processes, or LSASS access from an untrusted binary.
- Endpoint isolation, process termination, credential resets, and forensic acquisition belong to authorized incident responders.

## 4. Document

Record evidence, validated context, false-positive rationale, confidence, escalation owner, and rule-tuning recommendation.
