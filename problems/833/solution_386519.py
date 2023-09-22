def conta_numero(num,m):
     '''
Função que dado um número inteiro e uma matriz, retorna quantas vezes o número aparece na matriz.

int,list-->bool
    '''
     conta= 0
     l=len(m)
     c=len(m[0])
     for num in range(l):
    
            conta=num.count(num)
            for num in range(c):
                conta=num.count(num)
     return conta