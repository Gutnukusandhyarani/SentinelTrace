# Investigation 03 — Phishing Email and Network Evidence Review

<badge>Illustrative case study · static training example</badge>

## Case summary

**Case ID:** LAB-IR-003  
**Severity:** Medium (proposed; raise if user interaction or endpoint execution is confirmed)  
**Disposition:** Suspicious email; escalate for mail-gateway and endpoint correlation

## Part A — Email review

The following is a fabricated header/body example using the reserved `.test` domain:

```text
From: "IT Support" <helpdesk@corp-example.test>
Reply-To: password-reset@external-example.test
Return-Path: <bounce@external-example.test>
Subject: Action required: mailbox verification
Authentication-Results: spf=fail; dkim=none; dmarc=fail
Received: from mailer.external-example.test (198.51.100.23)
```

**Illustrative findings:**
- Display name and sender identity are not aligned with the example organization's domain.
- `Reply-To` differs from `From`.
- SPF, DKIM, and DMARC show failure in the fabricated header.
- A message that urges immediate action should be treated cautiously, but urgency alone is not proof of phishing.

No live domain, URL, file, or sender is provided in this exercise.

## Part B — Network/PCAP review

A real PCAP is not bundled with this pack. The following is a worksheet-style example of observations an analyst might document after reviewing an authorized training capture in Wireshark.

| Review item | Example observation | Analyst meaning |
|---|---|---|
| DNS | Host resolves a domain inconsistent with the claimed sender | Correlate with mail and endpoint records |
| HTTP | Request path contains a long opaque token | Preserve request metadata; do not browse to it |
| TLS | Certificate/SNI context does not match the claimed service | Validate certificate chain and destination ownership |
| Timing | Network request occurs shortly after message receipt | Supports correlation but does not prove a click |

**Useful Wireshark display filters for defensive review:**

```text
dns
http.request
tls.handshake.type == 1
ip.addr == 198.51.100.23
```

The example IP is documentation-only. Do not treat the example as a blocklist IOC.

## Verdict and confidence

**Proposed verdict:** Suspicious — escalate for validation.  
**Confidence:** Medium, because authentication failures and sender mismatch are indicators, but no actual recipient interaction, payload, or endpoint execution has been established.

## IOCs and evidence

| Type | Example | Status |
|---|---|---|
| Sender domain | `external-example.test` | Synthetic placeholder |
| Source IP | `198.51.100.23` | TEST-NET-2 documentation address |
| URL | Not supplied | Unknown |
| Attachment hash | Not supplied | Unknown |

## L1 actions

1. Preserve the original message and full headers through approved mail-security tooling.
2. Confirm recipients and whether anyone replied, clicked, or opened an attachment using authorized telemetry.
3. Review proxy/DNS/EDR records around the message time.
4. Do not open links or attachments as part of this exercise.
5. Escalate to the phishing response owner if user interaction or endpoint execution is confirmed.

## What I would improve

I would correlate the message ID, recipient, URL click telemetry, DNS/proxy records, and endpoint process events. I would avoid drawing a malware conclusion from a suspicious-looking header alone.
