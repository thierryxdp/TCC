def uppCons(frase):
    '''funcao que, dada uma frase, retorna essa mesma frase de entrada, porem com todas
    as consoantes em maiusculas;
    str->str'''
    texto=''
    letra=0
    while letra<len(frase):
        if frase[letra]not in'AaÁáEeÉéIiÍíOoÓóUuÚú':
            texto = texto + str.upper(frase[letra])
        else:
            texto = texto + frase[letra]
        letra=letra+1
    return texto