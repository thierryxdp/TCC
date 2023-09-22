def soma_h(n):
    '''funcao que recebe N inteiro como entrada 
    e retorna seu resultado somente com duas casas decimais 
    int-->float'''
    cont = 0
    for i in range (1, n+1):
        H = 1/i
        cont = cont + 1 
    return round (cont, 2)