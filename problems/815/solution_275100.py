def insere(lista_numero,n):
    """Função que dada uma lista ordenada de número inteiros e um novo número ineiro n, retorna uma nova lista crescente com o novo número inteiro adicionado.
    casos de teste:
    entrada:([1,3],2) saida: [1,2,3]
    entrada:([1,4,7], 5) saida: [1,4,5,7]
    entrada:([2,4,6,8],3) saida:[2.3.4.6.8]
    assinatura: list(int), int -> list(int"""
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero