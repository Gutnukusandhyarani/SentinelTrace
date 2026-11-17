# Investigation 01 — SSH Authentication Burst Followed by Success

<badge>Illustrative case study · synthetic telemetry</badge>

## Case summary

**Case ID:** LAB-IR-001  
**Severity:** Critical (proposed)  
**Disposition:** Suspicious authentication; escalate for account-owner validation  
**Host:** `lab-linux-01`  
**Source:** `203.0.113.45` (documentation-only address)  
**Account:** `analyst`

## Evidence timeline

| Time (UTC) | Source event | Observation |
|---|---|---|
| 10:00 | OpenSSH authentication failure | Invalid `admin` account |
| 10:01 | OpenSSH authentication failure | Invalid `admin` account |
| 10:02 | OpenSSH authentication failure | Invalid `admin` account |
| 10:03 | OpenSSH authentication failure | Invalid `admin` account |
| 10:04 | OpenSSH authentication failure | Invalid `admin` account |
| 10:05 | OpenSSH authentication success | `analyst` login from the same source |

All timestamps and entities above belong to a fabricated lab scenario. The source address is reserved for documentation and is not a live IOC.

## Detection result

**Triggered rules:** `SSH_BRUTE_FORCE` (High), `AUTH_SUCCESS_AFTER_FAILURES` (Critical)

**Illustrative SIEM alert output:**

```text
alert_id: AUTH_SUCCESS_AFTER_FAILURES
severity: CRITICAL
source_ip: 203.0.113.45
target_user: analyst
failed_attempts: 5
success_observed: true
time_window: 5 minutes
analyst_status: NEEDS_VALIDATION
```

## Analyst assessment

The combination of repeated failures and a later success from the same source raises concern for password guessing. It does not establish that the successful login was unauthorized. The source could be a shared NAT, approved test host, or user with stale credentials.

## L1 checklist

1. Validate the account owner and whether the login was expected.
2. Check the source address against VPN, NAT, scanner, and approved testing records.
3. Review MFA and authentication method, if collected.
4. Search a wider time window for other accounts and destination hosts.
5. Preserve relevant auth logs and escalate if the owner cannot validate the activity.

## Escalation note

> Potential password-guessing sequence observed on `lab-linux-01`: five SSH authentication failures from the same source were followed by a successful login to `analyst`. This is synthetic training evidence. Account-owner validation, MFA context, source ownership, and surrounding host activity are still required before declaring compromise.

## What I would improve

The initial rule groups by source IP. In a real environment, I would also correlate by account, host, VPN identity, and identity-provider telemetry to reduce noisy shared-egress alerts.
