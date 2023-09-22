def primo(numero):
    """função que retorna a quantidade de divisores de um numero
    int -> int"""
    lista=[]
    for n in range(2,numero):
        if (numero%n)==0:
            lista.append(n)
    if len(lista) > 0:
        return False
    else:
        return True