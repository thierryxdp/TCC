def uppCons(frase):
    """Função que recebe uma frase, retornado a mesma frase contendo todas as consoantes
    desta frase em maiusculas
    entrada: str
    retorno: str""" 
    i= 0
    frase_saida= ''
    while i< len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            frase_saida=frase[i].upper()
        else:
            frase_saida=frase[i]
        i = i+1
    return frase