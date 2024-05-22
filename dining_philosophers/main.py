"""Main module for dining_philosophers package"""

import sys
import signal

from .src.dining_philosophers import DiningPhilosophers
from .version import __version__ as version

def signal_handler(sig, frame) -> None:
    print("Ctrl+C keyboard interrupt. Exiting...")
    try:
        signal.default_int_handler(sig, frame)
    except KeyboardInterrupt:
        
        sys.exit(1)
signal.signal(signal.SIGINT, signal_handler)

def main():
    """Main function for dining_philosophers package"""
    args = sys.argv[1:]
    dining_philosophers = DiningPhilosophers()
    dining_philosophers.name = "Dining Philosophers"
    dining_philosophers.version = version
    if len(args) == 1:
        if args[0] == "deterministic":
            dining_philosophers.run_deterministic()
        elif args[0] == "random":
            dining_philosophers.run_random()
        elif args[0] == "showcase":
            dining_philosophers.run_showcase()
        elif args[0] == "version":
            print(f"{dining_philosophers.name} {dining_philosophers.version}")
        elif args[0] == "help":
            print(f"{dining_philosophers.name} {dining_philosophers.version}")
            print("Usage: python main.py [deterministic|random|showcase|load|version|help]")
        else:
            raise ValueError("Invalid argument")
    elif len(args) > 1:
        if args[0] == "load":
            if int(args[1]) == len(args) - 4:
                n = int(args[1])
                lambdas = [float(args[i]) for i in range(2, n + 2)]
                mi = float(args[n + 2])
                T = int(args[n + 3])
                dining_philosophers.run_deterministic(n, lambdas, mi, T)
            else:
                raise ValueError("Invalid number of arguments")
        else:
            raise ValueError("Invalid argument")
    else:
        dining_philosophers.run_deterministic()

if __name__ == "__main__":
    main()
