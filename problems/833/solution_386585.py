def conta_numero(numero,matriz):
    '''
Função que dado um numero inteiro e uma matriz retorna quantas x o numerp aparece na matriz

int,list-->bool
'''
    conta = 0
    
    for in range(len(matriz)):
        conta=conta+ list.count(i,numero)
        
        
        return conta