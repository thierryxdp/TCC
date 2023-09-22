def primo(n):
    if n%2=0:
        return 2<0
    i = 1
    s = 1
    while i < n:
        s= (s * i)
        i= i + 1
    return s%(n)==0