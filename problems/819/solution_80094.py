def filtraMultiplos(lista, numero):
    """Dada uma lista de números e um número, a função retorna uma
    nova lista contendo apenas os elementos da lista original que forem
    divisíveis pelo numero dado como parâmetro.
       A lista deve ser escrita entre colchetes [];
       list, float --> list"""
    listaNova = []
    proxnumero = 0
    while proxnumero<len(lista):
        if lista[proxnumero]%numero == 0:
            listaNova = listaNova + [lista[proxnumero],]
        proxnumero = proxnumero + 1
    return listaNova