def lingua_p(palavra):
    """Funcao recebe uma palavra e a traduz para a lingua do P """

    vogais = "aeiouãáâéíîóú"
    
    palavra = palavra.lower()

    traduzida = ""
    
    p = ""

    for numero in range(0, len(palavra)):
        if palavra[numero] in vogais:
            p = palavra[numero] + "p" + palavra[numero]
            traduzida += p
            p = ""
        else:
            traduzida += palavra[numero]
            
    return traduzida