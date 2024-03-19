import random
from src.stick import Stick
from src.philosopher import Philosopher

class DiningSimulation:
    def __init__(self, n, lambdas, mi, T):
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

    def simulate(self):
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