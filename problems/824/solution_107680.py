def uppCons(frase):
    """Funcao que retorna uma frase com suas consoantes em Maiusculo
    Entrada: str;
    Saida: str;
    
    Parameters:
    frase: Frase a ser modificada.
    """
    frase_Maiuscula = ''
    posicao = 0
    
    while posicao < len(frase):
        caracter = frase[posicao]
        if frase[posicao] in 'bcçdfghjklmnpqrstvwxyz':
            caracter = caracter.upper()
        frase_Maiuscula = frase_Maiuscula + caracter
        posicao = posicao + 1
    return frase_Maiuscula