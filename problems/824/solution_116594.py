#Questao 2
def uppCons(string):
    '''
    funcao que retorna a frase com todas as consoantes em maiúsculas. 
    str->str.
    '''
    j = 0
    x = ''
    while j < len(string):
        if string[j] in 'bcçdfghjklmnpqrstvwxyz':
            x = x + (string[j].upper())
        j = j + 1
    return string