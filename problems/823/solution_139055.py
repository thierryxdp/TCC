def faltante(lista):
    '''funcao que retorna o numero inteiro que esta faltando do intervalo da lista list->int'''
    i = 0
    
    L = []
    
    list.sort(lista)
    
    while i < len(lista) + 1:
        
        L = L +[i+1,]
        
    x = sum(L)
    
    y = sum(lista)
    
    return x - y