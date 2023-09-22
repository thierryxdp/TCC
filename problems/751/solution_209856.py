def quant_palavras(frase):
    '''recebe uma frase e retorna o número de 
    palavras da frase.
    string -> int'''
    qt = frase.strip().rstrip()
    return len(qt)