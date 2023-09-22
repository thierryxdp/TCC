def insere(lista_numero,n):
    """Função que ao receber uma lista crescente de números inteiros e
    um número inteiro, retorna a inclusão desse número inteiro na posição
    correta;
    list, int -> list"""
    lista_numero[2:2] = [n]
    list.sort(lista_numero)
    return lista_numero