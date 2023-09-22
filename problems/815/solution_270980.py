def insere(lista_numero,n):
    'função que dado uma lista de numeros e um numero inteiro n, retorna uma lista com todos os numeros em ordem crescente'
    lista_de_n = [n]
    lista_todos_os_numeros = lista_numero + lista_de_n
    lista_crescente = list.sort(lista_todos_os_numeros)
    return lista_crescente