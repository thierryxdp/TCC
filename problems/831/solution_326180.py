def lingua_p(palavra):
    """Retorna a palavra traduzida para lingua do P.
    Parametros:
    Entrada:str
    Saida:str"""
    palavra=str.lower(palavra)
    linguaP=str()
    for letra in palavra:
        if letra in "aeiouáéíóú":
            linguaP=linguaP+letra+"p"+letra
        else:
            linguaP=linguaP+letra
    return linguaP