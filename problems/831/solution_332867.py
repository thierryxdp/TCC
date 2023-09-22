def lingua_p(frase):
    """Função que retorna a palavra traduzida para lingua do P."""
    frase1 = frase
    for i in frase:
        if i in "aeiouAEIOU ":
            frase1 = frase1.replace(i,i+"p"+i)
    return frase1