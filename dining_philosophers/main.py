"""Main module for dining_philosophers package"""

from src.dining_simulation import DiningSimulation
from version import __version__ as version

def main():
    n = 5
    lambdas = [0.2, 0.3, 0.4, 0.5, 0.6]
    mi = 0.8
    T = 100

    sim = DiningSimulation(n, lambdas, mi, T)
    sim.simulate()

if __name__ == "__main__":
    main()
