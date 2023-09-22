def filtraMultiplos(lista,numero):
    '''Função que dados uma lista de números e um numero n,
    filtra e retorna os multiplos do numero n dentro da lista;
    list, int -> list'''

    listaA = []
    proximo = 0

    while proximo < len(lista):
          if lista[proximo]%numero == 0:
              listaA = listaA + [lista[proximo]]
          proximo = proximo + 1
    return listaA