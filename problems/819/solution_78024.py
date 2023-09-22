def filtraMultiplos(lista,n):
    """função que dada uma lista e um numero(n), retorne uma lista com os valores divisiveis por n da lista original;list,int-->list"""
    listaDivisiveis=()
    proximo=0
    while proximo<len(lista):
         if lista[proximo]%n==0:
            listaDivisiveis = listaDivisiveis+(lista[proximo],)
            proximo= proximo+1
    return listaDivisores