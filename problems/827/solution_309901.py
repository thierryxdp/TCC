def qtd_divisores (n):
    if n>0:
        a = list(range(n+1))
    if n<0 or n==0:
      	return 0
    list.remove (a, 0)
    r = 0
    for e in a:
        if n % e == 0:
            r = r+1
        else:
            r = r
    return r