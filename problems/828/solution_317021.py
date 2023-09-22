def primo(numero):
    '''Função que dado um numero inteiro positivo, verifica se esse
numero é primo ou não e retorna True ou False, respectivamente;
    int -> booleano'''
    for elemento in range(1,numero):
        if numero%elemento==0:
            p=False
        else:
            p=True
    return p