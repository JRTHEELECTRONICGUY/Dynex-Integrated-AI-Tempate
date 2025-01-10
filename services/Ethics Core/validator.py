
import json

class EthicsValidator:
    def __init__(self, config_path="services/ethics-core/config.json"):
        with open(config_path, 'r') as config_file:
            self.config = json.load(config_file)

    def validate_action(self, action_metadata):
        """
        Validate an action against the ethics rules.
        :param action_metadata: dict containing action details.
        :return: bool indicating whether the action is ethical.
        """
        for rule in self.config["ethics_rules"]:
            if not self._check_rule(action_metadata, rule):
                return False, f"Violation of rule: {rule['description']}"
        return True, "Action is ethical."

    def _check_rule(self, action_metadata, rule):
        """
        Check a specific rule.
        :param action_metadata: dict containing action details.
        :param rule: rule dict from the configuration.
        :return: bool
        """
        if rule["type"] == "prohibit" and action_metadata.get(rule["field"]) == rule["value"]:
            return False
        return True
