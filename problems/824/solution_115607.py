def uppCons(frase):
    '''função que recbe uma frase e retorna todas as consoantes
    em maiúsculo
    valor de entrada: str
    valor de saída: str'''
    proximo=0
    frasemudada=[]
    while proximo< len(frase):
        if str.lower(frasemudada[proximo]) not in 'aeiou':
            frasemudada.append(str.upper[proximo])
        else:
            frasemudada.append(frase[proximo])
        proximo= proximo+1
    return frasemudada.join(' ')