def filtra_pares(a):
    a = int(a[0])
    b = int(a[1])
    c = int(a[2])
    d = int(a[3])
    a1 = a%2
    b1 = b%2
    c1 = c%2
    d1 = d%2
    s = ('')
    if a == a1 + int(a[0]):
        s = (s,a)
    if b == b1 + b:
        s = (s,b)
    if c == c1 + c:
        s = (s,c)
    if d == d1 + d:
        s = (s,d)
    return s