def uppCons(frase):
    '''Recebe como entrada uma frase e retorna a frase com todas as suas
consoantes em maiúsculas e os demais caracteres exatamente como estavam na
frase original.'''
    i = 0
    vogal = ['a', 'e', 'i', 'o', 'u']
    acento = [ 'á', 'â', 'ã', 'é', 'ê', 'í', 'î', 'ó', 'ô', 'õ', 'ú', 'û']
    frase2 = ''
    while i < len(frase):
        if frase[i] not in vogal or acento:
            frase2 += frase[i].upper()
        else:
            frase2 += frase[i]
        i = i+1

    return frase2