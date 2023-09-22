def uppCons(frase):
    '''Calcula e retorna uma frase com todas as suas consoantes maiúsculas, aparti da frase fornecida.
    str-->str'''
    final=''
    i=0
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiou':
            conso=str.upper(frase[i])
            final=final+conso
        final=final+frase[i]
        i=i+1
    return final