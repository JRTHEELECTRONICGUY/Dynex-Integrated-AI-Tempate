
class BlockchainLogger:
    def __init__(self, blockchain_client):
        self.client = blockchain_client

    def log_event(self, event_data):
        """
        Log an event to the blockchain.
        :param event_data: dict containing event details.
        :return: str indicating log status.
        """
        try:
            transaction_hash = self.client.send_transaction(event_data)
            return f"Event logged to blockchain with transaction hash: {transaction_hash}"
        except Exception as e:
            return f"Blockchain logging failed: {str(e)}"
