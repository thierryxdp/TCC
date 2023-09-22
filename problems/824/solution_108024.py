def uppCons(frase):
    """Retorna a frase dada com todas as suas consoantes em maiuscula;
       Entrada: str;
       Saida: str
    """
    maiuscula = ' '
    posicao = 0
    while posicao < len(frase):
        consoante = frase[posicao]
        if frase[posicao] in 'bcdfghjklmnpqrstvwxyz':
            consoante.upper()
        maiuscula = maiuscula + consoante
        posicao = posicao + 1
    return maiuscula