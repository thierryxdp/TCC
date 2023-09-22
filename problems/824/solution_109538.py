def uppCons(frase):
    """Esta função receba uma frase e retorna esta frase com todas as consoantes em maiúsculo, sem alterar os outros caracteres
    str -> str"""
    for i in frase:
        if i not in "aeiouáàâãéíóúôêõ":
        	i = i.upper
    return frase