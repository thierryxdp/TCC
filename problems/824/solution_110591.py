def uppCons(frase):
    """Função que recebe uma frase e retorna a mesma
    com todas a suas consoantes em maiúsculo
    str -> str"""
    frase = frase.replace(' ', '_')
    frase_list = list(frase)
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    extencao = len(frase_list)
    contador = 0
    while contador < extencao:
        if frase_list[contador] in consoantes:
            frase_list[contador] = frase_list[contador].upper()
        contador += 1
    frase = frase.join('', frase_list)
    frase = frase.replace('_', ' ')
    return frase