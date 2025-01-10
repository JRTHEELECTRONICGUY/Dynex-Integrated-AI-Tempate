
import time

class Auditor:
    def __init__(self, log_file="audit_log.txt"):
        self.log_file = log_file

    def audit(self, system_state):
        """
        Audit the system for ethical compliance.
        :param system_state: dict representing the current state of the system.
        :return: bool indicating audit success.
        """
        with open(self.log_file, 'a') as log:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
            log.write(f"{timestamp} - Audit performed: {system_state}\n")
        
        if "critical_errors" in system_state and system_state["critical_errors"] > 0:
            return False
        return True
