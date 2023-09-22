def conta_frases(texto):
    """
    	Funcao que dado um texto, retorna o numero de frases 
        presentes no texto. As frases do texto sao separadas
        por: ".", "!", "?" e "...".
    """
    a= str.count(texto,".")
    b= str.count(texto,"!")
    c= str.count(texto,"?")
    d= str.count(texto,"...")
    return a + b + c + d + (d*(-3))