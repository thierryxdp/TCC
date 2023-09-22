def primo(n):
    '''Função que recebe um número int(n) positivo;
verifica se este número é primo ou não.
Retorna True se for primo e False caso contrário.
int->bool'''
    for i in range(2, n):
        if n %i==0:
            return False
    return True