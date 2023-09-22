def maiores(lista_numero, n):
    """Função que dada uma uma lista de números int retorna outra lista com os numeros da lista original
    list, int -> int"""
    list.append(lista_numero, n)
    list.sort(lista_numero)
    ocorrencia_a = list.index(lista_numero, n)+1
    return lista_numero[ocorrencia_a:]