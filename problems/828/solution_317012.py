def primo(numero):
    '''Função que dado um numero inteiro positivo, verifica se esse
numero é primo ou não e retorna True ou False, respectivamente;
    int -> booleano'''
    p=True
    for elemento in range(1,numero):
        if numero%elemento==0:
            p=False
    return p