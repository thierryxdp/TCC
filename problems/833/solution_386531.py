def conta_numero(num,m):
     '''
Função que dado um número inteiro e uma matriz, retorna quantas vezes o número aparece na matriz.

int,list-->bool
    '''
     conta= 0
     l=len(m)
     c=len(m[0])
     for i in range(l):
            for i in range(c):
                conta= list.count(i,num )
    
                
     return conta