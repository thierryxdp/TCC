def conta_frase(frase):
    """ """
    frase1=str.replace(frase,'?','/')
    frase2=str.replace(frase1,'!','/')
    frase3=str.replace(frase2,'...','/')
    frase4=str.replace(frase3,'.','/')
    frasefinal=str.split(frase4,'/')
    return len(frasefinal)-1