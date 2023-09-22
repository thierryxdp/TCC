def conta_numero(num,matriz):
     '''
Função que dado um número inteiro e uma matriz, retorna quantas vezes o número aparece na matriz.

int,list-->bool
    '''
     conta= 0
   
     for i in range(len(matriz)):
        conta=conta+ list.count(i,num)
        
            
     return conta