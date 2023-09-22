def conta_numero(num,matriz):
     '''
Função que dado um número inteiro e uma matriz, retorna quantas vezes o número aparece na matriz.

int,list-->int
    '''
     conta= 0
   
     for linha in matriz:
        conta=conta+list.count(linha,num)
        
           
     return conta