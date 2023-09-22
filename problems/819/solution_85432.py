#Função que dados uma lista de números e um numero n filtra e retorna os multiplos do numero n dentro da lista;lista = int
def filtraMultiplos(lista,numero):
    lista1 = []
    proximo = 0

    while proximo < len(lista):
          if lista[proximo]%numero == 0:
              lista1 = lista1 + [lista[proximo]]
          proximo = proximo + 1
    return lista1