def uppcons(FRASE):
    '''funcao que retorna as consoantes com letra maiuscula 
    str-->str.upper'''
    i=0
    consoantes=''
    White i<len(frase):
        if frase[i] in "bcdfghjklmnpqrstvwxyz":
            consoantes=consoantes+frase[i].upper()
        else:
            consoantes=consoantes+frase[i]
        i=i+l
    return consoantes