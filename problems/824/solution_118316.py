def eh_consoante(letra):
    return letra.lower() in "bcdfghjklmnpqrstvxwyz"

def uppCons(frase):
    '''retorna as consoantes da frase em maiusculo e nao altera as demais letras'''
    nova_frase = ' '
    i=0
    while i< len(frase):
        letra = frase[i]
        if eh_consoante(letra):
            letra = str.upper(letra)
        nova_frase += letra
        i+=1
    return nova_frase