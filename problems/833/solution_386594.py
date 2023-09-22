def conta_numero(num,matriz):
    '''
Função que dado um numero inteiro e uma matriz retorna quantas x o numerp aparece na matriz

int,list-->bool
'''
    conta = 0
    
    for num in matriz:
        conta=conta+ list.count(linha,num)
                                        
        
        return conta