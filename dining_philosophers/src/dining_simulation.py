"""Dining simulation class module"""

import random

from src.stick import Stick
from src.philosopher import Philosopher

class DiningSimulation:
    """Dining simulation class for dining philosophers problem"""
    
    def __init__(self, n, lambdas, mi, T) -> None:
        self.n = n
        self.lambdas = lambdas
        self.mi = mi
        self.T = T
        self.sticks = [Stick(i) for i in range(n)]
        self.philosophers = []
        for i in range(n):
            stick_1 = self.sticks[i]
            stick_2 = self.sticks[(i + 1) % n]
            self.philosophers.append(Philosopher(i, stick_1, stick_2))
        self.philosophers[-1].sticks[1] = self.sticks[0]
        self.__version : str | None = None
        self.__name : str | None = None
    
    @property
    def version(self) -> str:
        """Gets the version of the Feast"""
        return self.__version
    
    @version.setter
    def version(self, version : str) -> None:
        """Sets the version of the Feast"""
        self.__version = version
    
    @property
    def name(self) -> str:
        """Gets the name of the Feast"""
        return self.__name
    
    @name.setter
    def name(self, name : str) -> None:
        """Sets the name of the Feast"""
        self.__name = name

    def simulate(self) -> None:
        """Simulate dining philosophers problem for T time steps"""
        print(f"{self.name} {self.version} is running")
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
