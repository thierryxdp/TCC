def eh_quadrada(M):
    '''
    função que dada uma matriz M, retorna True caso ela seja quadrada, contando com a condição
    de uma matriz vazia (ou seja, sem nenhuma linha ou coluna), e retorna False caso ela
    não seja quadrada
    list(list)--> bool
    '''
    if M==[] or len(M)==len(M[0]):
        return True
    else:
        return False