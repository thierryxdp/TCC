def filtra_pares(numeros):
    'Recebe uma tupla contendo 4 numeros inteiros e retorna uma tupla contendo somente os que forem pares da tupla de entrada. (Int,int,int,int)->(n*int)
    w,x,y,z = numeros
    tupla_saida = ()
    if int(numeros[0])%2==0:
        tupla_saida = tupla_saida +(numeros[0],)
    if int(numeros[1])%2==0:
        tupla_saida = tupla_saida +(numeros[1],)
    if int(numeros[2])%2==0:
        tupla_saida = tupla_saida +(numeros[2],)
    if int(numeros[3])%2==0:
        tupla_saida = tupla_saida +(numeros[3],)
        return tupla_saida