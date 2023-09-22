def uppCons(frase):
    '''Função que dada uma frase de entrada, retorna a mesma frase com as
    consoantes maiúsculas.'''
    contador = 0
    frase_nova = ''
    while contador < len(frase):
        if frase[contador] not in 'AEIOUaeiouáéíóuãõâêôîû':
            maiuscula = frase[contador].upper()
            frase_nova = frase_nova + maiuscula
        else:
            frase_nova = frase_nova + frase[contador]
        contador = contador + 1
    return frase_nova