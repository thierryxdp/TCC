def qtd_divisores(n):
    """funcao que conta a quantidade de divisores do numero n dado.
    int -> int"""
    lista = []
    contagem = 0
    while contagem < n:
        if n%(contagem+1)==0:
            list.append(lista, contagem+1)
        contagem +=1
    return len(lista)