def filtraMultiplos(listan,n):
    '''Funcao que dada uma lista de numeros e um numero
    retorna uma outra lista contendo todos os elementos da
    lista original que sao multiplos de n
    Parametros:
    List, Float
    Saida: list
    '''
    m=[]
    p= 0
    while p < len(listan):
        if listan[p]%n ==0:
            m= m + [listan[p]]
        p= p+1
    
    return m