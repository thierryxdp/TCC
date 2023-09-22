def melhor_volta(matriz):
    '''A função retornará qual foi o corredor com o menor tempo (1 à 6), qual esse menor tempo
    e em qual volta isso ocorreu
    Dados de entrada -> lista
    Dados de saída -> tupla (int, int, int)'''
    
    lista_menor = []
    
    for i in range(6):
        menor = min(matriz[i])
        lista_menor += [menor]
        
    menor_todos = min(lista_menor)
    
    indice_menor = list.index(lista_menor,menor_todos)
    indice_menor1 = list.index(lista_menor,menor_todos) + 1
    
    volta_menor = list.index(matriz[indice_menor],menor_todos) + 1
    
    return (indice_menor1,menor_todos,volta_menor)