def uppCons (frase):
    '''receb uma frase e retorna a mesma frase com todas as suas consoantes em maisculo e as demais letras exatamente como estavam'''
    '''str->str'''
    i=0
    vogais=''
    while i<len(texto):
        if texto[i] in 'AEIOUaeiou':
            vogais=vogais+texto[i]
        i=i+1
    return vogais