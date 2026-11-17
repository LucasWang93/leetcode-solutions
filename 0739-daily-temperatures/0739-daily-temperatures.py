class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answers = [0] * n
        stk = []

        for i in range(n-1, -1, -1):
            while stk and (temperatures[stk[-1]] <= temperatures[i]):
                # answers[stk[-1]] = i - stk[-1]
                stk.pop()
            if stk:
                answers[i] = stk[-1] - i
            stk.append(i)

        return answers
        
        
        
        
        
        
        
        
        
        
        # n = len(temperatures)
        # answer = [0] * n
        # stk = []
        # for i in range(n-1, -1, -1):
        #     while stk and temperatures[stk[-1]] <= temperatures[i]:
        #         stk.pop()
        #     answer[i] = 0 if not stk else stk[-1] - i
        #     stk.append(i)
        # return answer
        