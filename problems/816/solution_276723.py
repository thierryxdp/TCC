def maiores(lista,n):
    """Função que retorna uma lista com os números maiores que o n dado
    em ordem crescente:lista,int->list"""
    resultado = []
    for i in range(len(lista)):
        if lista[i]>n:
            resultado.append(lista[i])

    resultado= sorted(resultado)
    return resultado