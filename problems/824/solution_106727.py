def uppCons(frase):
    '''Função que, dada uma frase, retorna ela com as consoantes maiúsculas.
    str --> str'''
    i = 0
    frase_nova = ''
    while i < len(frase):
        if frase[i] in 'aeiouAEIOUãáâàéêíîóôõúÃÁÂÀÉÊÍÎÓÔÕÚ':
            frase_nova = frase_nova + frase[i]
        else:
            frase_nova = frase_nova + str.upper(frase[i])
        i = i + 1
    return frase_nova