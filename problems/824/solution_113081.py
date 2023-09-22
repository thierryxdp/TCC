def uppCons(frase):
    i = 0
    consoante = ''
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            consoante += str.upper(frase[i])
            i+=1
        elif frase[i] not in 'bcdfghjklmnpqrstvwxyz':
            consoante += frase[i]
            i+=1
  		return consoante