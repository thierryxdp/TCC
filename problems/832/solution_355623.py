def eh_quadrada(a):
    if a==[]:
        return True
    elif len(a)==len(a[0]) and a!=[]:
        return True
    elif len(a)!=len(a[0]) and a!=[]:
        return False