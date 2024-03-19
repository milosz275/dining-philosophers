"""Main module for dining_philosophers package"""

from src.feast import Feast
from version import __version__ as version

def main():
    """Executes main function"""
    app = Feast()
    app.set_version(version)
    app.run()
    return

if __name__ == "__main__":
    main()
