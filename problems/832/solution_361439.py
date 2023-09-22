def eh_quadrada(M):
    """Função que recebe uma matriz formada por listas e retorna um valor
    booleano que diz se essa matriz é quadrada ou não.
    list -> bool"""
    if M==[]:
        return True
    if len(M)==1:
        return True
    else:
        return len(M)== len(M[0])