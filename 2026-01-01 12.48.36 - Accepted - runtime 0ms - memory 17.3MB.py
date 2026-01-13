class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        first_pos = {}
        for i, c in enumerate(s):
            if c in first_pos:
                actual_dist = i - first_pos[c] - 1
                expected_dist = distance[ord(c) - ord('a')]
                if actual_dist != expected_dist:
                    return False
            else:
                first_pos[c] = i
        return True