def uppCons(texto):
    """funcao que recebe uma string e retorna essa string com todas as consoantes
    em maiusculos, e os demais caracteres do jeito original. string->string"""
    consoantes=''
    proximo=0
    while proximo<len(texto):
        if texto[proximo] in 'bcdfgjklmnpqrstvwxz':
            consoantes= consoantes+str.upper(texto[proximo])
        if texto[proximo] in 'aeiouh':
            consoantes= consoantes+texto[proximo]
        proximo= proximo+1
    return consoantes