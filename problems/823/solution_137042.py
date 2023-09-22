def faltante(lista):
    """Funcao que recebe de entrada uma lista de 1 a N e retorna qual numero inteiro esta faltando. list=>int"""
    if lista[0]!=1:
        return 1
    x=0
    while x<(len(lista)-1):
        if lista[x]+1==lista[x+1]:
            x=x+1
        else:
            return lista[x]+1
    else:
        return len(lista)+1