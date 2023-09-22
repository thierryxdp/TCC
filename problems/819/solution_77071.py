def filtraMultiplos(lista,n):
    """Função que recebe como entrada uma lista e um número 'n',
       retornando uma outra lista como todos os elementos da lista original 
       que forem divisíveis por 'n'
       Parâmetros de entrada:list
       Parâmetros de saída:list"""
    i=0
    proximo=0
    while i<len(lista):
        if l[proximo]%n==0:
            lista=lista+(l[proximo])
        proximo=proximo+1
    return lista