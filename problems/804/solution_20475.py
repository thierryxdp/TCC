def filtra_pares(tup):
    '''Função que recebe uma tupla com quatro números inteiros e retorna uma nova tupla com somente os números pares da tupla orignal, na mesma ordem em que se encontravam; tup->tuo'''
    final=()
    if tup[0]%2==0:
        final=(tup[0],)
       
    if tup[1]%2==0:
        final=(tup[1],)
        
    if tup[2]%2==0:
        final=(tup[2],)
        
    if tup[3]%2==0:
        final=(tup[3],)