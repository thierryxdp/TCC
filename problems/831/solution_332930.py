def lingua_p(frase):
    """
    """
    frase1 = frase
    for i in frase:
        if i in "aeiouAEIOU ":
          frase1 = frase1.replace(i,i+"p"+i)
    return frase1