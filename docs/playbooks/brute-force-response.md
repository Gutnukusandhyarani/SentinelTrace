# Playbook — Suspected Brute Force / Password Guessing

**Trigger:** Repeated authentication failures, especially when followed by a success.  
**ATT&CK:** T1110.001  
**Owner:** L1 SOC analyst; follow organization-specific escalation policy.

## 1. Validate

- Confirm source, destination, username, timestamps, failure count, and authentication result.
- Check whether source belongs to VPN, NAT, vulnerability scanner, identity provider, or approved test tooling.
- Confirm whether a success followed failures and whether MFA was completed.
- Check affected accounts and hosts for nearby alerts.

## 2. Classify

- **Likely benign:** approved testing or documented maintenance with a matching change record.
- **Suspicious:** unexplained high-volume failures or unusual account targeting.
- **High priority:** successful login after failures, privileged account, multiple hosts, or evidence of follow-on activity.

## 3. Respond

- Record evidence and analyst reasoning.
- Escalate confirmed or high-confidence suspicious activity.
- Account lockout, session revocation, password reset, and source blocking must be performed only by authorized responders under the approved process.
- Preserve relevant logs before retention windows expire.

## 4. Close

Record disposition, reason, evidence sources, owner, time, actions, and tuning recommendation.

## Required case fields

`case_id`, `alert_id`, `source_ip`, `target_user`, `destination_host`, `first_seen`, `last_seen`, `failure_count`, `success_after_failure`, `MFA_context`, `change_ticket`, `disposition`, `escalation_owner`.
