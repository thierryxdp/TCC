def qtd_divisores(n):
    lista =[]
    contagem = 0
    while contagem<n:
        if n%(contagem+1)==0:
            list.append(lista, contagem+1)
        contagem += 1
    return len(lista)

def primo(n):
    """funcao que dado um numero n retorna se ele é primo ou não.
    int -> bool"""
    a = qtd_divisores(n)
    if a == 2:
        return True
    else:
        return False