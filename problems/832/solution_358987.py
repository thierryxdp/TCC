def eh_quadrada(M):
    """Funcao que identifica se uma matriz M é quadrada. Uma 
    matriz vazia tambem e considerada quadrada. A funcao 
    retorna True, caso seja e False, caso nao seja;
    lista->bool"""
    
    if M==[]:
        return True
    elif len(M)==len(M[0]):
        return True
    else:
        return False