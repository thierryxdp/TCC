def uppCons(frase):
    '''funcao que recebe uma frase e retorna a frase com todas as suas consoantes em maiusculas
       : str -> str
    '''
    i = 0
    fraseM = ''
    while i < len(frase):
        frase = frase.replace(pontos[i], '1234567890')
        i=i+1
    total_frases = frase.count('1234567890')
    return total_frases