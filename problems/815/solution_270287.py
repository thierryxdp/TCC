def insere(lista_numero,n):
    """Função que recebe uma lista de numeros e adiciona um numero
    n e retorna e retorna em ordem crescente"""
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero