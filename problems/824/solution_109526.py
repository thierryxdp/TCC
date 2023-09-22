def uppCons(frase):
    '''Função que recebe uma frase e retorna a frase com todas suas
    consoantes em caixa alta
    str -> str'''
    novafrase= ''
    i=0
    while i<len(frase):
        if frase[i] in 'AEIOUaeiouÃÁÉÍÕÓÚãáéíõóú':
            novafrase= novafrase + frase[i]
        else:
            novafrase= novafrase + str.upper(frase[i])
        i= i+1
    return novafrase