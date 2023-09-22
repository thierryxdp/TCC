def uppCons(frase:str) -> str:
    """Essa função, dada uma frase como parâmetro de entrada,
    retorna a frase com todas as consoantes em maiúsculo"""
    i = 0
    while i < len(frase):
        if frase[i] in 'BbCcçÇDdFfGHhgJjKkLlMmNnPpQqRrSsTtVvWwXxZz':
            frase = frase.replace(frase[i], frase[i].upper())
        i += 1
    return frase