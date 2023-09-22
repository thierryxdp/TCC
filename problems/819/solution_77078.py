def filtraMultiplos(l,n):
    """Função que recebe como entrada uma lista e um número 'n',
       retornando uma outra lista como todos os elementos da lista original 
       que forem divisíveis por 'n'
       Parâmetros de entrada:list,int
       Parâmetros de saída:list"""
    lista=[]
    i=0
    proximo=0
    while i<len(l):
        if (l[i]%n==0):
            list.append(lista,l[i])
        i=i+1
    return lista