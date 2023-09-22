#Função que dado um número inteiro e uma matriz qualquer,conta quantas vezes o numero dado como entrada aparece na matriz, int,int = bool
def conta_numero(numero, matriz):
   
 contador = 0
    
    for i in matriz:
        
        for j in i:
            if numero == j:
                contador = contador + 1
    return contador