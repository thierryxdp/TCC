def filtraMultiplos(lista,n):
    """Dada uma lista contendo números inteiros e um número n inteiro como
    argumentos de entrada, a função retorna uma lista com apenas os 
    números múltiplos de n contidos na lista; 
    
    lista(int),int->lista(int)"""
    
    multiplos=[]
    proximo=0
    while proximo<len(lista):
        if lista[proximo]%n==0:
            multiplos=multiplos+[lista[proximo]]
        proximo=proximo+1
    return multiplos