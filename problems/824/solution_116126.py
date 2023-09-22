def uppCons(frase):
    '''Recebe como entrada uma frase e a retorna com suas consoantes  
    em maiúsculas
    str -> str'''
    posicao=0
    while posicao<len(frase):
        if frase(posicao) not in 'aeiouAEIOU:
            frase(posicao)=frase(posicao).upper()
        posicao=posicao+1
    return frase