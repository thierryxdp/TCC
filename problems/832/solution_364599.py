def eh_quadrada(M):
    '''Função que dada uma matriz M identifica se ela é uma 
matriz quadrada ou não e retornando, respectivamente, True ou
False;
	list -> booleano'''
    p=False
    if M==[]:
        p=True
    elif len(M)==len(M[0]):
            p=True
    return p