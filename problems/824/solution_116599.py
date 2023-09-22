def uppCons(frase):
    """dada uma frase retorna a mesma com todas as cosoantes em maiuscula"""
    i=0
    aux=''
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxywzç':
            aux += frase[i].upper()
        else:
            aux += frase[i]
        i+=1
    return aux