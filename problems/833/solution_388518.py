def conta_numero(numero, matriz):
    '''Função que dado um número inteiro e uma matriz qualquer,
    conta e retorna quantas vezees o número dado como entrada
    aparece na matriz; int, list -> int'''
    
    contador = 0
    
    for i in matriz:
        
        for j in i:
            if numero == j:
                contador = contador + 1
    return contador