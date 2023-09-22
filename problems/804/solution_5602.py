#---------------------EXERCICIO 6---------------------

def filtra_pares(int1,int2,int3,int4):
    '''recebe 4 elementos inteiros e retorna os pares
       <int,int,int,int> -> <>'''

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