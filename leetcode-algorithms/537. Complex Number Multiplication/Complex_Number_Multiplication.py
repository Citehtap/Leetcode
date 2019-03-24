class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        temp = a.split("+")
        reala = int(temp[0])
        imga = int(temp[1].split("i")[0])
        temp = b.split("+")
        realb = int(temp[0])
        imgb = int(temp[1].split("i")[0])
        real = reala * realb - imga * imgb
        img = reala * imgb + imga * realb
        return str(real) + "+" + str(img) + "i"