class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = deque()
        counter = defaultdict(int)
        res = 0
        for c in s:
            window.append(c)
            counter[c] += 1
            
            while counter[c] > 1:
                cur = window.popleft()
                counter[cur] -= 1

            res = max(res, len(window))

        return res
