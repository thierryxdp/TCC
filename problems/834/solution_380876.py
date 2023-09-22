#Função que retorna a média dos números presentes na matriz,lista = float
def media(matriz):
    
    lista = []
    
    for i in matriz:
        for j in i:
            lista = lista + [j]
   
    return  round(sum(lista) / len(lista),2)