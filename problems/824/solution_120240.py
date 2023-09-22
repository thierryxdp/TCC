def uppCons (frase):
    """funcao que recebe uma frase qualquer 
    e retorna uma frase com todas as consoantes em maiusculo
    str-> str"""
    contador = 0
    frase_nova = ''
    while contador < len(frase):
        if 'bcdfghjklmnpqrstvwxyz' in frase[contador]:
            frase_nova = str.join(frase_nova,frase[contador].upper)
        if 'aeiou' in frase[contador]:
            frase_nova = str.join(frase_nova,frase[contador])           
        contador += 1
        return frase_nova