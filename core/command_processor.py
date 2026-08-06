import json

class CommandProcessor:
    """
    Processes recognized commands into structured actions.
    """

    POLITE_WORDS = {
        "please",
        "kindly",
        "could",
        "would",
        "can"
    }
    def __init__(self):
        with open("data/commands.json","r") as file:
            self.commands = json.load(file)

    def _normalise(self,command):
        if not command:
            return ""
        cleaned_command  = command.strip()
        words = cleaned_command.split()
        filtered_command =[]
        for word in words:
            if word not in self.POLITE_WORDS:
                filtered_command.append(word)
        res = (" ").join(filtered_command)
        return res

    def process(self,command):
        normalised_command = self._normalise(command)
        if not normalised_command:
            return None
        if normalised_command in self.commands:
            return self.commands[normalised_command]
        return None