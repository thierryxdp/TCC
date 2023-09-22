def uppCons(frase):
    '''Recebe como entrada uma frase e a retorna com suas consoantes  
    em maiúsculas
    str -> str'''
    vogais='aAeEiIoOuU'
    posicao=0
    frase_nova=''
    while posicao<len(frase):
        if frase[posicao] not in vogais:
            frase_nova=frase_nova+frase[posicao].upper()
        else:
            frase_nova=frase_nova+frase[posicao]
        posicao=posicao+1
    return frase_nova