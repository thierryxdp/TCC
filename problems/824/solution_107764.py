def uppCons(frase): #Recebe uma frase
    frasefinal = []
    for letra in frase:
        frasefinal.append(letra)
        if letra in 'bcdfghjklmnpqrstvwxyz':
            letrafinal = letra.upper()
            frasefinal.remove(letra)
            frasefinal.append(letrafinal)
    frasefinal = ''.join(frasefinal)
    return frasefinal #Retorna a frase com as consoantes em maiúsculo