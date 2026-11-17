# Playbook — Suspected Phishing Email

**Trigger:** User report, mail-security alert, sender-authentication anomaly, or suspicious URL/attachment metadata.

## 1. Validate the message

- Preserve the original message and complete headers using approved mail tooling.
- Review sender, reply-to, return-path, message ID, sending infrastructure, and SPF/DKIM/DMARC results.
- Check recipient scope and whether a campaign affected multiple mailboxes.
- Treat domains, URLs, and attachment names as untrusted evidence. Do not visit suspicious links or open attachments.

## 2. Establish impact

- Determine whether the user replied, clicked, submitted credentials, or opened an attachment from approved audit records.
- Correlate email time with proxy, DNS, identity, and endpoint telemetry.
- Record any confirmed accounts, hosts, URLs, domains, and file hashes.

## 3. Escalate and contain

- Escalate suspected credential theft, confirmed user interaction, or endpoint execution.
- Message quarantine, URL blocking, password reset, token revocation, and endpoint isolation are actions for authorized responders under local procedure.
- Do not delete evidence before the investigation owner approves.

## 4. Close

Document affected users, evidence, scope, verdict, confidence, actions, lessons learned, and detection-tuning opportunities.
