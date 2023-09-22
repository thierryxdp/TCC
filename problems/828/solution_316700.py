def primo(numero):
    '''Função que dado um numero inteiro positivo, verifica se esse
numero é primo ou não, e retorna True ou False, respectivamente;
    int -> booleano'''
    for elemento in range(numero):
        if numero%2==0:
            return 'False'
        else:
            return 'True'