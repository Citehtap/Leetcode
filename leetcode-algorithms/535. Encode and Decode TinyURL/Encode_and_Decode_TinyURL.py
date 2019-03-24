"""
创建两个映射map1,map2，map1代表id1:longUrl，map2代表shortUrl:id2。
encode时，令id2反复对62求余（数字与大小写字母共62个字符），根据余数取字母；
decode时，根据shortUrl的长度得到longUrl。
"""
class Codec:
    map1 = {}
    map2 = {}
    s = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if (not longUrl in self.map1):
            self.map1[len(self.map1) + 1] = longUrl
            self.map2[longUrl] = len(self.map2) + 1

        n = self.map2.get(longUrl)
        str = ""
        while n > 0:
            r = int(n % 62)
            n = int(n / 62)
            str = self.s[r] + str
        return str

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        length = len(shortUrl)
        index = 0
        for i in range(0, length):
            index = index * 62 + self.s.index(shortUrl[i])
        return self.map1.get(index)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))