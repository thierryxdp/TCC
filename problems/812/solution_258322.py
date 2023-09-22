retira_pontuacao (frase):
    """funcao que substitue os caracteres por espacos
    str -> str"""
    carac=[".",":",";","!","_",",","?"]
    frase = list(frase)
    
    for i in range (0,len(frase)):
        for j in range (0,len(carac)):
            if frase[i] == carac[j]:
                frase[i]=" "
                return "".join(frase)