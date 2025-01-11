import logging
import json
from datetime import datetime

# Load configuration file
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Set up logging
logging.basicConfig(
    level=getattr(logging, config["ethics_core"]["logging"]["log_level"]),
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Auditor:
    def __init__(self):
        self.audit_enabled = config["ethics_core"]["logging"]["enable_blockchain_audit"]
        self.log_retention_days = config["ethics_core"]["logging"]["log_retention_days"]

    def record_action(self, user, action, status, metadata=None):
        """
        Records an action for auditing purposes.
        """
        audit_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "user": user,
            "action": action,
            "status": "SUCCESS" if status else "FAILURE",
            "metadata": metadata or {}
        }

        # Log to console or file
        logging.info(f"AUDIT RECORD: {audit_entry}")

        # Optionally, send to blockchain for immutable audit trail
        if self.audit_enabled:
            self._send_to_blockchain(audit_entry)

    def _send_to_blockchain(self, audit_entry):
        """
        Sends an audit entry to the blockchain.
        (Simulated; replace with actual blockchain interaction logic.)
        """
        try:
            # Simulate sending to blockchain
            logging.info(f"Sending audit entry to blockchain: {audit_entry}")
            # Actual blockchain integration logic would go here
        except Exception as e:
            logging.error(f"Failed to send audit entry to blockchain: {e}")

    def cleanup_logs(self):
        """
        Removes logs older than the configured retention period.
        """
        # Simulate log cleanup (customize as needed for file-based logging)
        logging.info(f"Cleaning up logs older than {self.log_retention_days} days.")
        # Add actual log file cleanup logic here


# Example usage
if __name__ == "__main__":
    auditor = Auditor()

    # Record a successful action
    auditor.record_action(
        user="test_user",
        action="sensitive_operation",
        status=True,
        metadata={"details": "Performed a critical operation successfully."}
    )

    # Record a failed action
    auditor.record_action(
        user="test_user",
        action="malicious_attempt",
        status=False,
        metadata={"reason": "Malicious actions are prohibited by ethics core."}
    )

    # Perform log cleanup
    auditor.cleanup_logs()
