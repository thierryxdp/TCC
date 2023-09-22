def filtraMultiplos(lista_numeros, numero):
    '''Recebe 2 parâmetros e retorna uma lista contento todos os elementos da 
    lista_numeros que é divisível por numero
    lista, float -> lista'''
    
    lista = []
    i = 0
    proximo = 0
    
    while lista_numeros[i]%numero == 0:
        list.append(lista, lista_numeros[i]) 
        i = i + 1
   
    return lista