def melhor_volta(matriz):
    
    lista_menor = []
    
    for i in range(6):
        menor = min(matriz[i])
        lista_menor += [menor]
        
    menor_todos = min(lista_menor)
    indice_menor = list.index(lista_menor,menor_todos)
    
    return (indice_menor,menor_todos)