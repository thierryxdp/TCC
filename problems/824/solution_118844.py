def uppCons(frase):
    mudado = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            mudado += char.upper() # transforma em maiúscula
        else: # não é consoante minúscula, mantém como no original
            mudado += char
    return mudado