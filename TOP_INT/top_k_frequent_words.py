from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[int]:
        c = Counter(words)

        q = []

        for kkk, v in c.items():
            heapq.heappush(q, (-1 * v, kkk))

        return [heappop(q)[1] for _ in range(k)]


