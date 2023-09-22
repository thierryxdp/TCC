# Questão3
def insere(lista_numero, n):
    """Função que ordene números inteiros incluindo o número
    'n';
    list, int -> list"""
    lista_numero[len(lista_numero):len(lista_numero)] = [n]
    return list.sort(lista_numero)