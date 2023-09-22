#Exercício_05:
''' Essa função insere um número "n" numa lista de forma tal que ela contínua ordenada de maneira crescente. '''
''' list, float ---> list. '''

def insere(lista_numero, n):
    
    #Adicionando o termo a lista:
    list.extend(lista_numero, [n])
    
    #Ordenando a lista:
    list.sort(lista_numero)
    
    #Retornando:
    return lista_numero