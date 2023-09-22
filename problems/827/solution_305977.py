def qtd_divisores(n):
    """funcao que conta quantos divisores um numero tem, este numero sera dado
    na entrada(n). int->int"""
    dvs=0
    lista=[]
    for divisores in range(1,n+1):
        if n%divisores==0:
            list.extend(lista,[divisores])
    return len(lista)