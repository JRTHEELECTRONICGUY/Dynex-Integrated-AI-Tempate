import logging
import json
import requests  # Assumes you will use an API to interact with the blockchain
from datetime import datetime

# Load configuration file
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Set up logging
logging.basicConfig(
    level=getattr(logging, config["ethics_core"]["logging"]["log_level"]),
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class BlockchainLogger:
    def __init__(self):
        self.blockchain_endpoint = config["blockchain"]["endpoint"]
        self.api_key = config["blockchain"].get("api_key", None)
        self.enabled = config["ethics_core"]["logging"]["enable_blockchain_audit"]

    def log_to_blockchain(self, user, action, status, metadata=None):
        """
        Sends a log entry to the blockchain for immutability.
        """
        if not self.enabled:
            logging.warning("Blockchain logging is disabled in the configuration.")
            return False

        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "user": user,
            "action": action,
            "status": "SUCCESS" if status else "FAILURE",
            "metadata": metadata or {}
        }

        try:
            # Send the log entry to the blockchain
            response = self._send_to_blockchain(log_entry)

            if response.status_code == 200:
                logging.info(f"Successfully logged to blockchain: {log_entry}")
                return True
            else:
                logging.error(f"Failed to log to blockchain. Status code: {response.status_code}, Response: {response.text}")
                return False
        except Exception as e:
            logging.error(f"Error logging to blockchain: {e}")
            return False

    def _send_to_blockchain(self, log_entry):
        """
        Handles the actual API call to the blockchain.
        """
        headers = {
            "Content-Type": "application/json",
        }
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        response = requests.post(
            url=self.blockchain_endpoint,
            headers=headers,
            data=json.dumps(log_entry)
        )
        return response


# Example usage
if __name__ == "__main__":
    blockchain_logger = BlockchainLogger()

    # Log a successful action
    blockchain_logger.log_to_blockchain(
        user="test_user",
        action="sensitive_operation",
        status=True,
        metadata={"details": "Performed a critical operation successfully."}
    )

    # Log a failed action
    blockchain_logger.log_to_blockchain(
        user="test_user",
        action="unauthorized_access_attempt",
        status=False,
        metadata={"reason": "Attempted unauthorized access to secure resource."}
    )
