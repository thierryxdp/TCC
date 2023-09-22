def primo(inteiro_positivo):
    '''função que ferifica se um número é primo, a partir de um parâmetro inteiro e positivo, retornando um valor booleano; int -> bool'''
    
    for i in range(2, inteiro_positivo):
        if not inteiro_positivo%i == 0:
            return False
        else:
            return False
    return True