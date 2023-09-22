def filtra_pares(i):
    ''' Função que dada uma tupla (i) que contenha 4 elementos
    inteiros retorna apenas os elementos pares
    Entrada: tupla (int,int,int,int)
    Retorno: tupla (*) *o número de elementos é igual ao número de elementos pares '''
    
    resto_elemento1 = i[0]%2
    resto_elemento2 = i[1]%2
    resto_elemento3 = i[2]%2
    resto_elemento4 = i[3]%2
    
    if