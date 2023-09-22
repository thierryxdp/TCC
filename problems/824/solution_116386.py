def uppCons(frase:str)->str:
    '''Funcao que retorna a frase em maiusculo exceto as vogais'''
    posicao=0
    final=''
    while posicao<len(frase):
        
        if frase[posicao] in 'aeiou':
            final= final + frase[posicao].lower()
        else:
            final= final+ frase[posicao].upper()
        posicao+=1
        
    return final