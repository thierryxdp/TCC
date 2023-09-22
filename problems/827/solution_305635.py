def qtd_divisores(n):
    """funcao que conta quantos divisores um numero tem, este numero sera dado
    na entrada(n). int->int"""
    soma=1
    lista=[]
    while soma<=n:
        if n%soma==0:
            list.extend(lista,[soma])
        soma += 1
    return len(lista)