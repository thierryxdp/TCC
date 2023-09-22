def maiores(lista,num):
    """Função que, dada uma lista de números inteiros e um número 'n', retorna
outra lista que contenha apenas os números da lista maiores que 'n'."""
    """list-->list"""
    resultado=[]
    for c in lista:
        if c > num:
            resultado.append(c)
    list.sort(resultado)
    return resultado