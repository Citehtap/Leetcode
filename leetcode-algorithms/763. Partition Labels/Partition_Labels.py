'''
字母区间为从起始位置到flag，遍历过程中更新flag
'''


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = {}
        result = [-1]
        for i in range(len(S)):
            last[S[i]] = i
        flag = last[S[0]]
        for w in range(len(S)):
            if w < flag:
                if last[S[w]] > flag:
                    flag = last[S[w]]
            if w == flag:
                result.append(flag)
                result[len(result)-2] = result[len(result)-1] - result[len(result)-2]
                if flag + 1 < len(S):
                    flag = last[S[flag+1]]
        result.pop()
        return result
