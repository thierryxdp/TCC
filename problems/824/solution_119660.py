def uppCons(frase):
    """Função que recebe como entrada uma frase e retorna a frase com todas
    as suas consoantes em maiúsculas (e os demais caracteres exatamente como
    estavam na frase original);
    str -> str"""
    contador = 0
    novaFrase = ''
    while contador < len(frase):
        if frase[contador] not in 'aeiouãéíóú':
            novaFrase += frase[contador].upper()
        else:
            novaFrase += frase[contador].lower()
        contador += 1

    return novaFrase