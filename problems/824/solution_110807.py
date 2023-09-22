def uppCons(frase):
    """Funcao que retorna uma frase com todas as suas consoantes em
    maiusculas e os demais caracteres exatamente como estavam na frase
    original); str -> str"""
    i = 0
    while i<len(frase):
        if frase[i] not in "AEIOUÃÕÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛaeiouãõáéíóúàèìòùâêîôû ":
            frase = str.replace(frase, frase[i],str.upper(frase[i]))
        i = i + 1
    return frase