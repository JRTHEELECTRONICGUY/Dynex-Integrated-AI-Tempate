
class Replicator:
    def __init__(self):
        self.replicas = 0

    def replicate(self, replication_metadata):
        """
        Perform a self-replication process with safeguards.
        :param replication_metadata: dict containing replication details.
        :return: str indicating the replication status.
        """
        if not replication_metadata.get("approved"):
            return "Replication denied: Ethics core requires approval."

        self.replicas += 1
        return f"Replication successful. Current replicas: {self.replicas}"

    def monitor_replicas(self):
        """
        Monitor the number of active replicas.
        :return: int
        """
        return self.replicas
