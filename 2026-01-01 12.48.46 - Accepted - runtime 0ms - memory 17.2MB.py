class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        pos = {}
        for i, c in enumerate(s):
            if c in pos:
                actual_dist = i - pos[c] - 1
                if actual_dist != distance[ord(c) - ord('a')]:
                    return False
            else:
                pos[c] = i
        return True