def uppCons(frase):
    """essa função irá colocar todas as consoantes em maiuscula em uma frase ou palavra
    entrada -> string
    saida -> string """
    i=0
    frase1=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxyzw':
            frase1 = frase1 + str.upper(frase[i])
        if frase[i] in ' aeiouãé,!?.íAEIOUúBCDFGHJKLMNPQRSTVXYZW':
            frase1 = frase1 + frase[i]
        i = i+1
    return frase1