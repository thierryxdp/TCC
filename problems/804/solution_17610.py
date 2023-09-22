'''
	A função filtra os elementos pares de uma tupla a e
    forma uma nova tupla com eles na ordem que aparecem em a.
    a -> uma tupla com quatro algarismos
    tupla -> tupla
'''
def filtra_pares(a):
    if a[0]%2==0:
        b=(a[0],)
    else:
        b=()
    if a[1]%2==0:
        c=b+(a[1])
    else:
        c=b
    if a[2]%2==0:
        d=c+(a[2])
    else:
        d=c
    if a[3]%2==0:
        e=d+(a[3])
    else:
        e=d
    return e