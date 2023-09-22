def conta_frases(texto):
    '''funcao que recebe uma frase e retorna o numero de frases que compoem esse texto
    str -> int'''
    fim_frase='.','!','?','...'
    return len(str.split(texto,fim_frase))