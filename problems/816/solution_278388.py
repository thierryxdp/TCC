def maiores(num,n):
    num.append(n)
    num.sort()
    return num[(num.index(n)+1):]