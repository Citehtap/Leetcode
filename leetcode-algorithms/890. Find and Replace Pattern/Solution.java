// 将pattern和word中的字母一一对应，同时判断是否有多个字母映射到同一个字母上。
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        result = []
        for word in words:
            d = {}
            flag = True
            for i in range(len(word)):
                if not pattern[i] in d:
                    if word[i] in d.values():
                        flag = False
                        break
                    else:
                        d[pattern[i]] = word[i]
                else:
                    if d[pattern[i]] != word[i]:
                        flag = False
                        break
            if flag:
                result.append(word)
        return result