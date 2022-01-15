# Find the area of an n-interesting polygon

def shapeArea(n):
    if n == 1:
        return n
    else:
        res = 0
        for i in range(1, n):
            res += 2 * ((2 * i) - 1)
        res += (2 * n) - 1
        return res

if __name__ == "__main__":
    print(shapeArea(4))
