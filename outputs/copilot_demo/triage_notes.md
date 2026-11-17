# SentinelTrace — Draft Triage Notes

> Draft suggestions only. A human analyst must validate evidence and choose the final disposition.

## LAB-TP-01

**Suggested verdict:** TRUE_POSITIVE  
**Confidence:** 0.78  
**Summary:** Repeated authentication failures followed by a successful login on lab-host-01  

**Likely cause:** The supplied signals contain suspicious behavior that warrants incident investigation.

**Evidence:**
- `rule_id=ST-DET-01`
- `severity=Critical`
- `host=lab-host-01`
- `user=analyst1`
- `src_ip=198.51.100.1`
- `timestamp=2026-11-17T10:05:00Z`
- `summary=Repeated authentication failures followed by a successful login on lab-host-01`
- `failed_attempts=7`
- `approved_change=False`

**Next steps:**
- Validate the source fields and collect surrounding endpoint or authentication events.
- Check account, host, and change-control context.
- Escalate to the incident owner; do not take containment action from this suggestion alone.

**Questions:**
- Can the account owner confirm the activity?
- Are there related alerts or successful logons on other hosts?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-TP-02

**Suggested verdict:** TRUE_POSITIVE  
**Confidence:** 0.78  
**Summary:** Repeated authentication failures followed by a successful login on lab-host-02  

**Likely cause:** The supplied signals contain suspicious behavior that warrants incident investigation.

**Evidence:**
- `rule_id=ST-DET-01`
- `severity=Critical`
- `host=lab-host-02`
- `user=analyst2`
- `src_ip=198.51.100.2`
- `timestamp=2026-11-17T10:05:00Z`
- `summary=Repeated authentication failures followed by a successful login on lab-host-02`
- `failed_attempts=7`
- `approved_change=False`

**Next steps:**
- Validate the source fields and collect surrounding endpoint or authentication events.
- Check account, host, and change-control context.
- Escalate to the incident owner; do not take containment action from this suggestion alone.

**Questions:**
- Can the account owner confirm the activity?
- Are there related alerts or successful logons on other hosts?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-TP-03

**Suggested verdict:** TRUE_POSITIVE  
**Confidence:** 0.78  
**Summary:** Repeated authentication failures followed by a successful login on lab-host-03  

**Likely cause:** The supplied signals contain suspicious behavior that warrants incident investigation.

**Evidence:**
- `rule_id=ST-DET-01`
- `severity=Critical`
- `host=lab-host-03`
- `user=analyst3`
- `src_ip=198.51.100.3`
- `timestamp=2026-11-17T10:05:00Z`
- `summary=Repeated authentication failures followed by a successful login on lab-host-03`
- `failed_attempts=7`
- `approved_change=False`

**Next steps:**
- Validate the source fields and collect surrounding endpoint or authentication events.
- Check account, host, and change-control context.
- Escalate to the incident owner; do not take containment action from this suggestion alone.

**Questions:**
- Can the account owner confirm the activity?
- Are there related alerts or successful logons on other hosts?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-TP-04

**Suggested verdict:** TRUE_POSITIVE  
**Confidence:** 0.78  
**Summary:** Repeated authentication failures followed by a successful login on lab-host-04  

**Likely cause:** The supplied signals contain suspicious behavior that warrants incident investigation.

**Evidence:**
- `rule_id=ST-DET-01`
- `severity=Critical`
- `host=lab-host-04`
- `user=analyst4`
- `src_ip=198.51.100.4`
- `timestamp=2026-11-17T10:05:00Z`
- `summary=Repeated authentication failures followed by a successful login on lab-host-04`
- `failed_attempts=7`
- `approved_change=False`

**Next steps:**
- Validate the source fields and collect surrounding endpoint or authentication events.
- Check account, host, and change-control context.
- Escalate to the incident owner; do not take containment action from this suggestion alone.

**Questions:**
- Can the account owner confirm the activity?
- Are there related alerts or successful logons on other hosts?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-TP-05

**Suggested verdict:** TRUE_POSITIVE  
**Confidence:** 0.78  
**Summary:** Repeated authentication failures followed by a successful login on lab-host-05  

**Likely cause:** The supplied signals contain suspicious behavior that warrants incident investigation.

**Evidence:**
- `rule_id=ST-DET-01`
- `severity=Critical`
- `host=lab-host-05`
- `user=analyst5`
- `src_ip=198.51.100.5`
- `timestamp=2026-11-17T10:05:00Z`
- `summary=Repeated authentication failures followed by a successful login on lab-host-05`
- `failed_attempts=7`
- `approved_change=False`

**Next steps:**
- Validate the source fields and collect surrounding endpoint or authentication events.
- Check account, host, and change-control context.
- Escalate to the incident owner; do not take containment action from this suggestion alone.

**Questions:**
- Can the account owner confirm the activity?
- Are there related alerts or successful logons on other hosts?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-TP-06

**Suggested verdict:** TRUE_POSITIVE  
**Confidence:** 0.78  
**Summary:** Repeated authentication failures followed by a successful login on lab-host-06  

**Likely cause:** The supplied signals contain suspicious behavior that warrants incident investigation.

**Evidence:**
- `rule_id=ST-DET-01`
- `severity=Critical`
- `host=lab-host-06`
- `user=analyst6`
- `src_ip=198.51.100.6`
- `timestamp=2026-11-17T10:05:00Z`
- `summary=Repeated authentication failures followed by a successful login on lab-host-06`
- `failed_attempts=7`
- `approved_change=False`

**Next steps:**
- Validate the source fields and collect surrounding endpoint or authentication events.
- Check account, host, and change-control context.
- Escalate to the incident owner; do not take containment action from this suggestion alone.

**Questions:**
- Can the account owner confirm the activity?
- Are there related alerts or successful logons on other hosts?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-TP-07

**Suggested verdict:** TRUE_POSITIVE  
**Confidence:** 0.78  
**Summary:** Repeated authentication failures followed by a successful login on lab-host-07  

**Likely cause:** The supplied signals contain suspicious behavior that warrants incident investigation.

**Evidence:**
- `rule_id=ST-DET-01`
- `severity=Critical`
- `host=lab-host-07`
- `user=analyst7`
- `src_ip=198.51.100.7`
- `timestamp=2026-11-17T10:05:00Z`
- `summary=Repeated authentication failures followed by a successful login on lab-host-07`
- `failed_attempts=7`
- `approved_change=False`

**Next steps:**
- Validate the source fields and collect surrounding endpoint or authentication events.
- Check account, host, and change-control context.
- Escalate to the incident owner; do not take containment action from this suggestion alone.

**Questions:**
- Can the account owner confirm the activity?
- Are there related alerts or successful logons on other hosts?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-TP-08

**Suggested verdict:** TRUE_POSITIVE  
**Confidence:** 0.78  
**Summary:** Repeated authentication failures followed by a successful login on lab-host-08  

**Likely cause:** The supplied signals contain suspicious behavior that warrants incident investigation.

**Evidence:**
- `rule_id=ST-DET-01`
- `severity=Critical`
- `host=lab-host-08`
- `user=analyst8`
- `src_ip=198.51.100.8`
- `timestamp=2026-11-17T10:05:00Z`
- `summary=Repeated authentication failures followed by a successful login on lab-host-08`
- `failed_attempts=7`
- `approved_change=False`

**Next steps:**
- Validate the source fields and collect surrounding endpoint or authentication events.
- Check account, host, and change-control context.
- Escalate to the incident owner; do not take containment action from this suggestion alone.

**Questions:**
- Can the account owner confirm the activity?
- Are there related alerts or successful logons on other hosts?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-TP-09

**Suggested verdict:** TRUE_POSITIVE  
**Confidence:** 0.78  
**Summary:** Repeated authentication failures followed by a successful login on lab-host-09  

**Likely cause:** The supplied signals contain suspicious behavior that warrants incident investigation.

**Evidence:**
- `rule_id=ST-DET-01`
- `severity=Critical`
- `host=lab-host-09`
- `user=analyst9`
- `src_ip=198.51.100.9`
- `timestamp=2026-11-17T10:05:00Z`
- `summary=Repeated authentication failures followed by a successful login on lab-host-09`
- `failed_attempts=7`
- `approved_change=False`

**Next steps:**
- Validate the source fields and collect surrounding endpoint or authentication events.
- Check account, host, and change-control context.
- Escalate to the incident owner; do not take containment action from this suggestion alone.

**Questions:**
- Can the account owner confirm the activity?
- Are there related alerts or successful logons on other hosts?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-TP-10

**Suggested verdict:** TRUE_POSITIVE  
**Confidence:** 0.78  
**Summary:** Repeated authentication failures followed by a successful login on lab-host-10  

**Likely cause:** The supplied signals contain suspicious behavior that warrants incident investigation.

**Evidence:**
- `rule_id=ST-DET-01`
- `severity=Critical`
- `host=lab-host-10`
- `user=analyst10`
- `src_ip=198.51.100.10`
- `timestamp=2026-11-17T10:05:00Z`
- `summary=Repeated authentication failures followed by a successful login on lab-host-10`
- `failed_attempts=7`
- `approved_change=False`

**Next steps:**
- Validate the source fields and collect surrounding endpoint or authentication events.
- Check account, host, and change-control context.
- Escalate to the incident owner; do not take containment action from this suggestion alone.

**Questions:**
- Can the account owner confirm the activity?
- Are there related alerts or successful logons on other hosts?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-FP-01

**Suggested verdict:** FALSE_POSITIVE  
**Confidence:** 0.88  
**Summary:** Scheduled task creation during approved endpoint maintenance on lab-host-01  

**Likely cause:** The supplied alert context indicates an approved change or maintenance activity.

**Evidence:**
- `rule_id=ST-DET-04`
- `severity=Medium`
- `host=lab-host-01`
- `user=SYSTEM`
- `src_ip=192.0.2.20`
- `timestamp=2026-11-17T11:00:00Z`
- `summary=Scheduled task creation during approved endpoint maintenance on lab-host-01`
- `failed_attempts=0`
- `approved_change=True`

**Next steps:**
- Verify the referenced change record and approved operator.
- Confirm the activity stayed within the change scope.
- Close as expected activity only after independent validation.

**Questions:**
- Does the change record match the host, account, and timestamp?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-FP-02

**Suggested verdict:** FALSE_POSITIVE  
**Confidence:** 0.88  
**Summary:** Scheduled task creation during approved endpoint maintenance on lab-host-02  

**Likely cause:** The supplied alert context indicates an approved change or maintenance activity.

**Evidence:**
- `rule_id=ST-DET-04`
- `severity=Medium`
- `host=lab-host-02`
- `user=SYSTEM`
- `src_ip=192.0.2.20`
- `timestamp=2026-11-17T11:00:00Z`
- `summary=Scheduled task creation during approved endpoint maintenance on lab-host-02`
- `failed_attempts=0`
- `approved_change=True`

**Next steps:**
- Verify the referenced change record and approved operator.
- Confirm the activity stayed within the change scope.
- Close as expected activity only after independent validation.

**Questions:**
- Does the change record match the host, account, and timestamp?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-FP-03

**Suggested verdict:** FALSE_POSITIVE  
**Confidence:** 0.88  
**Summary:** Scheduled task creation during approved endpoint maintenance on lab-host-03  

**Likely cause:** The supplied alert context indicates an approved change or maintenance activity.

**Evidence:**
- `rule_id=ST-DET-04`
- `severity=Medium`
- `host=lab-host-03`
- `user=SYSTEM`
- `src_ip=192.0.2.20`
- `timestamp=2026-11-17T11:00:00Z`
- `summary=Scheduled task creation during approved endpoint maintenance on lab-host-03`
- `failed_attempts=0`
- `approved_change=True`

**Next steps:**
- Verify the referenced change record and approved operator.
- Confirm the activity stayed within the change scope.
- Close as expected activity only after independent validation.

**Questions:**
- Does the change record match the host, account, and timestamp?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-FP-04

**Suggested verdict:** FALSE_POSITIVE  
**Confidence:** 0.88  
**Summary:** Scheduled task creation during approved endpoint maintenance on lab-host-04  

**Likely cause:** The supplied alert context indicates an approved change or maintenance activity.

**Evidence:**
- `rule_id=ST-DET-04`
- `severity=Medium`
- `host=lab-host-04`
- `user=SYSTEM`
- `src_ip=192.0.2.20`
- `timestamp=2026-11-17T11:00:00Z`
- `summary=Scheduled task creation during approved endpoint maintenance on lab-host-04`
- `failed_attempts=0`
- `approved_change=True`

**Next steps:**
- Verify the referenced change record and approved operator.
- Confirm the activity stayed within the change scope.
- Close as expected activity only after independent validation.

**Questions:**
- Does the change record match the host, account, and timestamp?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-FP-05

**Suggested verdict:** FALSE_POSITIVE  
**Confidence:** 0.88  
**Summary:** Scheduled task creation during approved endpoint maintenance on lab-host-05  

**Likely cause:** The supplied alert context indicates an approved change or maintenance activity.

**Evidence:**
- `rule_id=ST-DET-04`
- `severity=Medium`
- `host=lab-host-05`
- `user=SYSTEM`
- `src_ip=192.0.2.20`
- `timestamp=2026-11-17T11:00:00Z`
- `summary=Scheduled task creation during approved endpoint maintenance on lab-host-05`
- `failed_attempts=0`
- `approved_change=True`

**Next steps:**
- Verify the referenced change record and approved operator.
- Confirm the activity stayed within the change scope.
- Close as expected activity only after independent validation.

**Questions:**
- Does the change record match the host, account, and timestamp?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-FP-06

**Suggested verdict:** FALSE_POSITIVE  
**Confidence:** 0.88  
**Summary:** Scheduled task creation during approved endpoint maintenance on lab-host-06  

**Likely cause:** The supplied alert context indicates an approved change or maintenance activity.

**Evidence:**
- `rule_id=ST-DET-04`
- `severity=Medium`
- `host=lab-host-06`
- `user=SYSTEM`
- `src_ip=192.0.2.20`
- `timestamp=2026-11-17T11:00:00Z`
- `summary=Scheduled task creation during approved endpoint maintenance on lab-host-06`
- `failed_attempts=0`
- `approved_change=True`

**Next steps:**
- Verify the referenced change record and approved operator.
- Confirm the activity stayed within the change scope.
- Close as expected activity only after independent validation.

**Questions:**
- Does the change record match the host, account, and timestamp?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-FP-07

**Suggested verdict:** FALSE_POSITIVE  
**Confidence:** 0.88  
**Summary:** Scheduled task creation during approved endpoint maintenance on lab-host-07  

**Likely cause:** The supplied alert context indicates an approved change or maintenance activity.

**Evidence:**
- `rule_id=ST-DET-04`
- `severity=Medium`
- `host=lab-host-07`
- `user=SYSTEM`
- `src_ip=192.0.2.20`
- `timestamp=2026-11-17T11:00:00Z`
- `summary=Scheduled task creation during approved endpoint maintenance on lab-host-07`
- `failed_attempts=0`
- `approved_change=True`

**Next steps:**
- Verify the referenced change record and approved operator.
- Confirm the activity stayed within the change scope.
- Close as expected activity only after independent validation.

**Questions:**
- Does the change record match the host, account, and timestamp?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-FP-08

**Suggested verdict:** FALSE_POSITIVE  
**Confidence:** 0.88  
**Summary:** Scheduled task creation during approved endpoint maintenance on lab-host-08  

**Likely cause:** The supplied alert context indicates an approved change or maintenance activity.

**Evidence:**
- `rule_id=ST-DET-04`
- `severity=Medium`
- `host=lab-host-08`
- `user=SYSTEM`
- `src_ip=192.0.2.20`
- `timestamp=2026-11-17T11:00:00Z`
- `summary=Scheduled task creation during approved endpoint maintenance on lab-host-08`
- `failed_attempts=0`
- `approved_change=True`

**Next steps:**
- Verify the referenced change record and approved operator.
- Confirm the activity stayed within the change scope.
- Close as expected activity only after independent validation.

**Questions:**
- Does the change record match the host, account, and timestamp?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-FP-09

**Suggested verdict:** FALSE_POSITIVE  
**Confidence:** 0.88  
**Summary:** Scheduled task creation during approved endpoint maintenance on lab-host-09  

**Likely cause:** The supplied alert context indicates an approved change or maintenance activity.

**Evidence:**
- `rule_id=ST-DET-04`
- `severity=Medium`
- `host=lab-host-09`
- `user=SYSTEM`
- `src_ip=192.0.2.20`
- `timestamp=2026-11-17T11:00:00Z`
- `summary=Scheduled task creation during approved endpoint maintenance on lab-host-09`
- `failed_attempts=0`
- `approved_change=True`

**Next steps:**
- Verify the referenced change record and approved operator.
- Confirm the activity stayed within the change scope.
- Close as expected activity only after independent validation.

**Questions:**
- Does the change record match the host, account, and timestamp?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-FP-10

**Suggested verdict:** FALSE_POSITIVE  
**Confidence:** 0.88  
**Summary:** Scheduled task creation during approved endpoint maintenance on lab-host-10  

**Likely cause:** The supplied alert context indicates an approved change or maintenance activity.

**Evidence:**
- `rule_id=ST-DET-04`
- `severity=Medium`
- `host=lab-host-10`
- `user=SYSTEM`
- `src_ip=192.0.2.20`
- `timestamp=2026-11-17T11:00:00Z`
- `summary=Scheduled task creation during approved endpoint maintenance on lab-host-10`
- `failed_attempts=0`
- `approved_change=True`

**Next steps:**
- Verify the referenced change record and approved operator.
- Confirm the activity stayed within the change scope.
- Close as expected activity only after independent validation.

**Questions:**
- Does the change record match the host, account, and timestamp?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-ESC-01

**Suggested verdict:** ESCALATE  
**Confidence:** 0.52  
**Summary:** Alert requires context validation on lab-host-01  

**Likely cause:** The evidence is incomplete and does not support a confident true-positive or false-positive decision.

**Evidence:**
- `rule_id=ST-DET-02`
- `severity=High`
- `host=lab-host-01`
- `user=unknown`
- `src_ip=203.0.113.1`
- `timestamp=2026-11-17T12:00:00Z`
- `summary=Alert requires context validation on lab-host-01`
- `failed_attempts=1`
- `approved_change=False`

**Next steps:**
- Collect the missing host, user, process, and timeline context.
- Check the approved-change and asset-owner records.
- Escalate if the required context is unavailable within the response target.

**Questions:**
- What additional telemetry or change record can validate this event?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-ESC-02

**Suggested verdict:** ESCALATE  
**Confidence:** 0.52  
**Summary:** Alert requires context validation on lab-host-02  

**Likely cause:** The evidence is incomplete and does not support a confident true-positive or false-positive decision.

**Evidence:**
- `rule_id=ST-DET-05`
- `severity=High`
- `host=lab-host-02`
- `user=unknown`
- `src_ip=203.0.113.2`
- `timestamp=2026-11-17T12:00:00Z`
- `summary=Alert requires context validation on lab-host-02`
- `failed_attempts=1`
- `approved_change=False`

**Next steps:**
- Collect the missing host, user, process, and timeline context.
- Check the approved-change and asset-owner records.
- Escalate if the required context is unavailable within the response target.

**Questions:**
- What additional telemetry or change record can validate this event?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-ESC-03

**Suggested verdict:** ESCALATE  
**Confidence:** 0.52  
**Summary:** Alert requires context validation on lab-host-03  

**Likely cause:** The evidence is incomplete and does not support a confident true-positive or false-positive decision.

**Evidence:**
- `rule_id=ST-DET-02`
- `severity=High`
- `host=lab-host-03`
- `user=unknown`
- `src_ip=203.0.113.3`
- `timestamp=2026-11-17T12:00:00Z`
- `summary=Alert requires context validation on lab-host-03`
- `failed_attempts=1`
- `approved_change=False`

**Next steps:**
- Collect the missing host, user, process, and timeline context.
- Check the approved-change and asset-owner records.
- Escalate if the required context is unavailable within the response target.

**Questions:**
- What additional telemetry or change record can validate this event?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-ESC-04

**Suggested verdict:** ESCALATE  
**Confidence:** 0.52  
**Summary:** Alert requires context validation on lab-host-04  

**Likely cause:** The evidence is incomplete and does not support a confident true-positive or false-positive decision.

**Evidence:**
- `rule_id=ST-DET-05`
- `severity=High`
- `host=lab-host-04`
- `user=unknown`
- `src_ip=203.0.113.4`
- `timestamp=2026-11-17T12:00:00Z`
- `summary=Alert requires context validation on lab-host-04`
- `failed_attempts=1`
- `approved_change=False`

**Next steps:**
- Collect the missing host, user, process, and timeline context.
- Check the approved-change and asset-owner records.
- Escalate if the required context is unavailable within the response target.

**Questions:**
- What additional telemetry or change record can validate this event?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-ESC-05

**Suggested verdict:** ESCALATE  
**Confidence:** 0.52  
**Summary:** Alert requires context validation on lab-host-05  

**Likely cause:** The evidence is incomplete and does not support a confident true-positive or false-positive decision.

**Evidence:**
- `rule_id=ST-DET-02`
- `severity=High`
- `host=lab-host-05`
- `user=unknown`
- `src_ip=203.0.113.5`
- `timestamp=2026-11-17T12:00:00Z`
- `summary=Alert requires context validation on lab-host-05`
- `failed_attempts=1`
- `approved_change=False`

**Next steps:**
- Collect the missing host, user, process, and timeline context.
- Check the approved-change and asset-owner records.
- Escalate if the required context is unavailable within the response target.

**Questions:**
- What additional telemetry or change record can validate this event?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-ESC-06

**Suggested verdict:** ESCALATE  
**Confidence:** 0.52  
**Summary:** Alert requires context validation on lab-host-06  

**Likely cause:** The evidence is incomplete and does not support a confident true-positive or false-positive decision.

**Evidence:**
- `rule_id=ST-DET-05`
- `severity=High`
- `host=lab-host-06`
- `user=unknown`
- `src_ip=203.0.113.6`
- `timestamp=2026-11-17T12:00:00Z`
- `summary=Alert requires context validation on lab-host-06`
- `failed_attempts=1`
- `approved_change=False`

**Next steps:**
- Collect the missing host, user, process, and timeline context.
- Check the approved-change and asset-owner records.
- Escalate if the required context is unavailable within the response target.

**Questions:**
- What additional telemetry or change record can validate this event?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-ESC-07

**Suggested verdict:** ESCALATE  
**Confidence:** 0.52  
**Summary:** Alert requires context validation on lab-host-07  

**Likely cause:** The evidence is incomplete and does not support a confident true-positive or false-positive decision.

**Evidence:**
- `rule_id=ST-DET-02`
- `severity=High`
- `host=lab-host-07`
- `user=unknown`
- `src_ip=203.0.113.7`
- `timestamp=2026-11-17T12:00:00Z`
- `summary=Alert requires context validation on lab-host-07`
- `failed_attempts=1`
- `approved_change=False`

**Next steps:**
- Collect the missing host, user, process, and timeline context.
- Check the approved-change and asset-owner records.
- Escalate if the required context is unavailable within the response target.

**Questions:**
- What additional telemetry or change record can validate this event?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-ESC-08

**Suggested verdict:** ESCALATE  
**Confidence:** 0.52  
**Summary:** Alert requires context validation on lab-host-08  

**Likely cause:** The evidence is incomplete and does not support a confident true-positive or false-positive decision.

**Evidence:**
- `rule_id=ST-DET-05`
- `severity=High`
- `host=lab-host-08`
- `user=unknown`
- `src_ip=203.0.113.8`
- `timestamp=2026-11-17T12:00:00Z`
- `summary=Alert requires context validation on lab-host-08`
- `failed_attempts=1`
- `approved_change=False`

**Next steps:**
- Collect the missing host, user, process, and timeline context.
- Check the approved-change and asset-owner records.
- Escalate if the required context is unavailable within the response target.

**Questions:**
- What additional telemetry or change record can validate this event?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-ESC-09

**Suggested verdict:** ESCALATE  
**Confidence:** 0.52  
**Summary:** Alert requires context validation on lab-host-09  

**Likely cause:** The evidence is incomplete and does not support a confident true-positive or false-positive decision.

**Evidence:**
- `rule_id=ST-DET-02`
- `severity=High`
- `host=lab-host-09`
- `user=unknown`
- `src_ip=203.0.113.9`
- `timestamp=2026-11-17T12:00:00Z`
- `summary=Alert requires context validation on lab-host-09`
- `failed_attempts=1`
- `approved_change=False`

**Next steps:**
- Collect the missing host, user, process, and timeline context.
- Check the approved-change and asset-owner records.
- Escalate if the required context is unavailable within the response target.

**Questions:**
- What additional telemetry or change record can validate this event?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

## LAB-ESC-10

**Suggested verdict:** ESCALATE  
**Confidence:** 0.52  
**Summary:** Alert requires context validation on lab-host-10  

**Likely cause:** The evidence is incomplete and does not support a confident true-positive or false-positive decision.

**Evidence:**
- `rule_id=ST-DET-05`
- `severity=High`
- `host=lab-host-10`
- `user=unknown`
- `src_ip=203.0.113.10`
- `timestamp=2026-11-17T12:00:00Z`
- `summary=Alert requires context validation on lab-host-10`
- `failed_attempts=1`
- `approved_change=False`

**Next steps:**
- Collect the missing host, user, process, and timeline context.
- Check the approved-change and asset-owner records.
- Escalate if the required context is unavailable within the response target.

**Questions:**
- What additional telemetry or change record can validate this event?

**Unknowns:**
- The mock provider does not query a SIEM, EDR, identity provider, or threat-intelligence service.
- The alert context has not been independently verified.

---

