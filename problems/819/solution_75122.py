def filtraMultiplos(lista,n):
    """Função que recebe uma lista de numeros e um número n e retorna outra lista apenas com os números da lista original que forem divisíveis por n;list,int->list"""
    multiplos=[]
    proximo=0
    while proximo<len(lista):
        if lista[proximo]%n==0:
            multiplos=multiplos+[lista[proximo],]
        proximo = proximo + 1
    return multiplos