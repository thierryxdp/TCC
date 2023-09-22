def filtraMutiplos(lista,n):
    '''Recebe uma lista de números e um número n, e retorna
    outra lista contendo todos os elementos da lista original
    que forem divisiveis por n
    list, int -> list'''
    
    lista_f=[]
    i=0
    
    while i<len(lista):
        if lista[i]%n==0:
                lista_f=lista_f+lista[i]
        i=i+1
        
    return lista_f