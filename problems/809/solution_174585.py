def intercala(lista1,lista2):
    """ dada duas lista vamos intercala elas e colocar em ordem
        entrada --> int (lista)
        saida   --> int (lista)"""
    nova_lista = lista1 + lista2
    list.sort(nova_lista)
    return nova_lista



""" teste
    resultados esperados:
    resultados obtidos: """