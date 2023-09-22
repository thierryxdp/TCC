def primo(numero):
    '''Função que dado um numero inteiro positivo, verifica se esse
numero é primo ou não e retorna True ou False, respectivamente;
    int -> booleano'''
    q=0
    p=True
    for elemento in range(1,numero+1):
        if numero%elemento==0:
            q=q+1
        if q>2:
            p=False
    return p