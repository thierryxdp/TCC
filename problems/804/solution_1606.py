def filtra_pares(tupla):
    primeiro_termo = tupla[0]
    segundo_termo = tupla[1]
    terceiro_termo = tupla[2]
    quart_termo = tupla[3]
    #A função recebe os indices das tuplas
    
    tupla2 = ()
    if(primeiro_termo % 2 == 0):
        tupla2 += (primeiro_termo, )
    if(segundo_termo % 2 == 0):
        tupla2 += (segundo_termo, )
    if(terceiro_termo % 2 == 0):
        tupla2 += (terceiro_termo, )
    if(quart_termo % 2 == 0):
        tupla2 += (quart_termo, )
	#Avalia se os índices são pares ou não
    return tupla2
	#retorna uma nova tupla