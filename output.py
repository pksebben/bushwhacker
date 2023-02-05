"""Output control"""


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class Output:
    def __init__(self):
        # TODO: load config

        # colors
        self.HEADER = "\033[95m"
        self.OKBLUE = "\033[94m"
        self.OKCYAN = "\033[96m"
        self.OKGREEN = "\033[92m"
        self.WARNING = "\033[93m"
        self.FAIL = "\033[91m"
        self.ENDC = "\033[0m"
        self.BOLD = "\033[1m"
        self.UNDERLINE = "\033[4m"

        self.defaultcolor = self.BOLD

    def print(self, msg):
        print(f"{self.defaultcolor}{msg}{self.ENDC}")


printer = Output()
