from collections import deque


class RecentCounter():
    def __init__(self) -> None:
        self.q = deque()

    def ping(self, t: int):
        self.q.append(t)

        while self.q[0] < t - 3000:
            self.q.popleft()

        return len(self.q)
