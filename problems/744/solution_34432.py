def hashtag(s):
    '''Calcule e retorne uma função que receba uma string e insira o caractere # no início, no meio e no final'''
    meio = len(s) // 2
    return "#" + str([0:meio]) + "#" + str([meio:]) + "#"