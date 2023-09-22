def uppCons (frase):
    """funcao que recebe uma frase qualquer 
    e retorna uma frase com todas as consoantes em maiusculo
    str-> str"""
    contador = 0
    frase_nova = ''
    maiuscula = frase.upper
    while contador < len(frase):
        if 'A' or 'E' or 'I' or 'O' or 'U' in maiuscula[contador]:
            frase_nova = frase_nova + maiuscula[contador].lower
        contador += 1
        return frase_nova