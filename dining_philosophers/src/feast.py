"""Feast module for dining philosophers problem"""

class Feast():
    """Feast class for dining philosophers problem"""

    def __init__(self) -> None:
        self.__version : str = None
        return
    
    def set_version(self, version: str) -> None:
        """Set the version of the Feast"""
        self.__version = version
        return
    
    def version(self) -> str:
        """Get the version of the Feast"""
        return self.__version

    def run(self) -> None:
        """Run method for the Feast class"""
        print(f"Feast {self.version()} is running")
        return
