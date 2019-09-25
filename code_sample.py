class solution:
    def Add(self, x:int, y:int) -> int:
        while (y != 0):
            # carry
            carry = x&y
            # remain
            x = x^y
            # move carry to left
            y = carry << 1

        return x

if __name__ == '__main__':
    slt = solution()
    x=5
    y=6
    ret = slt.Add(x, y)
    print(ret)
