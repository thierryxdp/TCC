def pontos_por_time(lista):
    """A função que dado uma lista de 2 elementos, no
    formato especificado pela questao, retorna um dicionario
    com o número de pontos dos 2 jogos de cada time"""
    c=0
    f=0
    if(lista[0][2][0] > lista[0][2][1]):
        c=c+3
    if(lista[0][2][0] < lista[0][2][1]):
        f=f+3
    if(lista[0][2][0] == lista[0][2][1]):
        c=c+1
        f=f+1
    if(lista[1][2][0] < lista[1][2][1]):
        c=c+3
    if(lista[1][2][0] > lista[1][2][1]):
        f=f+3
    if(lista[1][2][1] == lista[1][2][0]):
        c=c+1
        f=f+1
    
    if(c>f):
    	dict1={
        	lista[0][0] : c ,
        	lista[0][1] : f
        	}
    else:
        dict1={
        	lista[1][0] : f ,
        	lista[1][1] : c
        	}
    return dict1