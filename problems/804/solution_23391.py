def filtra_pares(a,b,c,d):
    '''função que retorna nova tupla contendo apenas os elementos pares
    inseridos
    int,int,int,int->int'''
    if a/2==int and b/2==int and c/2==int and d/2==int:
        return a,b,c,d
    elif a/2==int and b/2==float and c/2==float and d/2==float:
        return a
    elif a/2==int and b/2==int and c/2==float and d/2==float:
        return a,b
    elif a/2==int and b/2==int and c/2==int and d/2==float:
        return a,b,c
    elif a/2==int and b/2==float and c/2==int and d/2==float:
        return a,c
    elif a/2==int and b/2==float and c/2==float and d/2==int:
        return a,d
    elif a/2==float and b/2==int and c/2==float and d/2==float:
        return b
    elif a/2==float and b/2==int and c/2==int and d/2==float:
        return b,c
    elif a/2==float and b/2==int and c/2==int and d/2==int:
        return b,c,d
    elif a/2==float and b/2==int and c/2==float and d/2==int:
        return b,d
    elif a/2==float and b/2==float and c/2==int and d/2==float:
        return c
    elif a/2==float and b/2==float and c/2==int and d/2==int:
        return c,d