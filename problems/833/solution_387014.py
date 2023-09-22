def conta_numero(numero,matriz):
    '''Recebe uma matriz e um número e retorna quantas 
    vezes ele apareceu'''
    #Conta o número de vezes que o número aparece
    contador=0
    #Percorre a matriz
    for i in matriz:
        #Conta quantas vezes se repete na lista
        contador+=i.count(numero)
    return contador