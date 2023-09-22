#---------------------EXERCICIO 6---------------------


def filtra_pares(numero):
    
    '''recebe 4 elementos inteiros e retorna os pares
       <int,int,int,int> -> <>'''
    
    int1=numero[0]
    int2=numero[1]
    int3=numero[2]
    int4=numero[3]
    
    tuplapar = ()
    
    if int1%2 == 0:
        tuplapar += (int1,)
    if int2%2 == 0:
        tuplapar += (int2,)
    if int3%2 == 0:
        tuplapar += (int3,)
    if int4%2 == 0:
        tuplapar += (int4,)
        
    return tuplapar