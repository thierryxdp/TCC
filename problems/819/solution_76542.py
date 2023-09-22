def filtraMultiplos(l,n):
    """Função que recebe como entrada uma lista 'l' de numeros e número 'n'
       e retorna outra lista, formada por todos os elementos da lista original
       que são divisíveis por 'n'
       Parâmetros de entrada: list,int
       Parâmetros de saída: list"""
    lista=[]
    proximo=0
    while proximo<len(lista):
        if l[proximo]%n==0:
            lista=lista+(l[proximo],)
        proximo=proximo+1
    return lista