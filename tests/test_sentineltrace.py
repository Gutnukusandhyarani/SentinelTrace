import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from sentineltrace import detect, parse_file, parse_line


class SentinelTraceTests(unittest.TestCase):
    def test_parses_ssh_failure(self):
        event = parse_line("Nov 11 10:00:00 host sshd[1]: Failed password for invalid user admin from 203.0.113.45 port 5000 ssh2")
        self.assertIsNotNone(event)
        self.assertEqual(event.event_type, "auth_failure")
        self.assertEqual(event.username, "admin")
        self.assertEqual(event.source_ip, "203.0.113.45")

    def test_ignores_unrelated_line(self):
        self.assertIsNone(parse_line("Nov 11 10:00:00 host systemd[1]: Started Service"))

    def test_sample_triggers_expected_rules(self):
        events = parse_file(ROOT / "data" / "sample_auth.log")
        alerts = detect(events)
        rules = {alert.rule_id for alert in alerts}
        self.assertEqual(len(events), 8)
        self.assertEqual(len(alerts), 3)
        self.assertEqual(rules, {
            "SSH_BRUTE_FORCE",
            "AUTH_SUCCESS_AFTER_FAILURES",
            "REMOTE_ROOT_LOGIN",
        })

    def test_normal_login_does_not_trigger_alert(self):
        event = parse_line("Nov 11 10:10:00 host sshd[8]: Accepted password for analyst from 192.168.1.25 port 51108 ssh2")
        self.assertEqual(detect([event]), [])

    def test_success_before_burst_completion_is_not_followup_alert(self):
        lines = [
            "Nov 11 10:00:00 host sshd[1]: Failed password for admin from 203.0.113.45 port 5001 ssh2",
            "Nov 11 10:01:00 host sshd[2]: Failed password for admin from 203.0.113.45 port 5002 ssh2",
            "Nov 11 10:02:00 host sshd[3]: Accepted password for analyst from 203.0.113.45 port 5003 ssh2",
            "Nov 11 10:03:00 host sshd[4]: Failed password for admin from 203.0.113.45 port 5004 ssh2",
            "Nov 11 10:04:00 host sshd[5]: Failed password for admin from 203.0.113.45 port 5005 ssh2",
            "Nov 11 10:05:00 host sshd[6]: Failed password for admin from 203.0.113.45 port 5006 ssh2",
        ]
        events = [parse_line(line) for line in lines]
        rules = {alert.rule_id for alert in detect(events)}
        self.assertIn("SSH_BRUTE_FORCE", rules)
        self.assertNotIn("AUTH_SUCCESS_AFTER_FAILURES", rules)


if __name__ == "__main__":
    unittest.main(verbosity=2)
