def uppCons(frase):
    """Transforma todas as letras consoantes em maiusculas. (str->str)"""
    letra=0
    frasenova=[]
    vocais=['a','e','i','o','u','á','à','â','ã','é','ê','í','ó','ô','õ','ú']
    while letra<len(frase):
        if frase[letra] not in vocais:
            frasenova.append(str.upper(frase[letra]))
            letra+=1
        else:
            frasenova.append(frase[letra])
            letra+=1
    return ''.join(frasenova)