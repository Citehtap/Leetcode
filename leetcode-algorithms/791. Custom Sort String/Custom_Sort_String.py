# 将T中的字符根据dct进行排序
class Solution:
    dct = {}

    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', \
                  'h', 'i', 'j', 'k', 'l', 'm', 'n', \
                  'o', 'p', 'q', 'r', 's', 't', 'u', \
                  'v', 'w', 'x', 'y', 'z']:
            self.dct[i] = 0
        for i in range(len(S)):
            self.dct[S[i]] = i
        return ''.join(self.QuickSort(T))

    def QuickSort(self, array):
        if len(array) < 2:
            return array
        else:
            base = self.dct[array[0]]
            less = [m for m in array[1:] if self.dct[m] < base]
            equal = [w for w in array if self.dct[w] == base]
            more = [n for n in array[1:] if self.dct[n] > base]
        return self.QuickSort(less) + equal + self.QuickSort(more)