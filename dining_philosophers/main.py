"""Main module for dining_philosophers package"""

from .src.dining_philosophers import DiningPhilosophers
from .version import __version__ as version

def main():
    """Main function for dining_philosophers package"""
    dining_philosophers = DiningPhilosophers()
    dining_philosophers.name = "Dining Philosophers"
    dining_philosophers.version = version
    dining_philosophers.run()

if __name__ == "__main__":
    main()
