def lingua_p(palavra:str)->str:
    '''Função que recebe uma palavra e retorna a mesma palavra traduzida para a língua do P.'''
    s=''
    for letra in palavra:
        if letra in'AEIOUaeiouáãéíóú':
            s=s+letra+'p'+letra
        else:
            s=s+letra
    return s