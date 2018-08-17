"""
https://mp.weixin.qq.com/s?__biz=MzI4Mzc5NDk4MA==&mid=2247484357&idx=6&sn=e51a2e0ff6df2a0337750f8435b73e3f&chksm=eb84088edcf3819865463152267a465b84e540c51795f071b608a74a5172ed513d84b1f52ba3&scene=0&pass_ticket=DyIzPNUSvFQ1Omhr%2FBlxdkV0W9zdMUF3O9qY45iaZQHu8nyBjFM2RX%2B34yHbso%2FC#rd
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
例如，给出 n = 3，生成结果为：
["((()))","(()())","(())()","()(())","()()()"]
"""

# 方法一：
class Solution(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0
        ans = []
        generate()
        return ans

# 方法二：
class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans
        
# 方法三：
class Solution(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans
