def filtrapares(tup):
    """j"""
    A,B,C,D= tup
    a=int(A)
    b=int(B)
    c=int(C)
    d=int(D)
    tuplapares=()
    if (a%2==0):
        tuplapares=tuplapares+(a,)
    if (b%2==0):
        tuplapares=tuplapares+(b,)
    if (c%2==0):
        tuplapares=tuplapares+(c,)
    if (d%2==0):
        tuplapares=tuplapares+(d,)
    return tuplapares