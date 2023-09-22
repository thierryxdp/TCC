def posLetra (frase,letra,num):
    '''função que dada uma string, letra e numero, retorne em 
    que posição da string aquela letra está dada a ocorrência
    string, string, int -> int'''
    pos = frase.find(letra)
    while pos >= 0 and num > 1:
            pos = frase.find(letra, pos +1)
            num -= 1
    return pos