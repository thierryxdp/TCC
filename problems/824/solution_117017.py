def uppCons(frase):
    '''dada uma frase, retorna a mesma frase mas com as consoantes em letra maniúscula'''
    if not 'aeiouAEIOU':
        return str.upper(frase)