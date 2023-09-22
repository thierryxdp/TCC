#Start your python function here
def filtra_pares(tupla):
    '''
    Recebe uma tupla com 4 elementos inteiros e retorna uma tupla só com os elementos pares.
    #Teste do primeiro elemento
    if(tupla[0]%2==0):
        lista.append(tupla[0])
    #Teste do segundo elemento    
    if(tupla[1]%2==0):
        lista.append(tupla[1])
    #Teste do terceiro elemento    
    if(tupla[2]%2==0):
        lista.append(tupla[2])
    #Teste do quarto elemento    
    if(tupla[3]%2==0):
        lista.append(tupla[3])
    '''
    lista = []
    if(tupla[0]%2==0):
        lista.append(tupla[0])
        
    if(tupla[1]%2==0):
        lista.append(tupla[1])
        
    if(tupla[2]%2==0):
        lista.append(tupla[2])
        
    if(tupla[3]%2==0):
        lista.append(tupla[3])
        
    return tuple(lista)