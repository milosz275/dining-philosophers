"""Module for dining simulation"""

import random
from typing import List

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import MultipleLocator

from .stick import Stick
from .philosopher import Philosopher

class DiningSimulation:
    """Dining simulation class for dining philosophers problem"""
    
    def __init__(self, n : int, lambdas : List[float], mi : float, T : int) -> None:
        self.n = n
        self.lambdas = lambdas
        self.mi = mi
        self.T = T
        self.sticks : List[Stick] = [Stick(i) for i in range(n)]
        self.philosophers : List[Philosopher] = []
        for i in range(n):
            stick_1 = self.sticks[i]
            stick_2 = self.sticks[(i + 1) % n]
            self.philosophers.append(Philosopher(i, stick_1, stick_2))
        self.philosophers[-1].sticks[1] = self.sticks[0]

    def simulate(self) -> None:
        """Simulates dining philosophers problem for T time steps"""
        for tic in range(self.T):
            for i in range(self.n):
                self.philosophers[i].asking_log.append(False)
                if self.philosophers[i].is_eating:
                    if random.random() < self.mi:
                        self.philosophers[i].stop_eating()
                elif random.random() < self.lambdas[i]:
                    self.philosophers[i].asking_log[tic]=True
                    if not self.philosophers[i].sticks[0].is_taken and not self.philosophers[i].sticks[1].is_taken:
                        self.philosophers[i].start_eating()
                self.philosophers[i].update_eating_log()
                
    def plot(self) -> None:
        """Plots the dining simulation using matplotlib"""
        matplotlib.use("TkAgg")
        
        plt.figure()
        plt.title("Dining Philosophers")
        plt.suptitle("Nikolai Lobchuk, Miłosz Maculewicz")
        plt.xlabel("Time")
        plt.ylabel("Philosopher")
        plt.grid(True)

        for i in range(self.n):
            j = 0
            start_x = [0, 0]
            while j < len(self.philosophers[i].eating_log):
                if j > 0 and self.philosophers[i].eating_log[j] and not self.philosophers[i].eating_log[j - 1]:
                    start_x[0] = j
                if j > 0 and not self.philosophers[i].eating_log[j] and self.philosophers[i].eating_log[j - 1]:
                    start_x[1] = j
                    plt.plot(start_x, [i + 1, i + 1], marker = 'o')
                if j == len(self.philosophers[i].eating_log) - 1 and self.philosophers[i].eating_log[j]:
                    start_x[1] = j
                    plt.plot(start_x, [i + 1, i + 1], marker = 'o')
                if not self.philosophers[i].eating_log[j] and self.philosophers[i].asking_log[j]:
                    plt.plot(j, i + 1, 'r^')
                j += 1

        plt.gca().xaxis.set_major_locator(MultipleLocator(5))
        plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
        plt.xlim(left=0)
        plt.xlim(right=100)
        plt.ylim(bottom=0)
        plt.ylim(top=self.n + 0.5)
        #plt.legend()
        plt.show()
