def uppCons(frase):
    i=0
    consoante=''
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            consoante += str.upper(frase[i])
            i+=1
        else:
            consoante += frase[i]
            i+=1
    return consoante