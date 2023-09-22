def uppCons(frase):
    """Função que recebe uma frase, retornado a mesma frase contendo todas as consoantes
    desta frase em maiusculas
    entrada: str
    retorno: str""" 
    i= 0
    return frase[i]
    while i< len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            frase.upper()
        i = i+1
    return frase