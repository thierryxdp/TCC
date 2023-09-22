def inverte(frase):
	"""
    Essa função inverte uma frase, contendo as mesmas palavras,
    porém em uma ordem inversa, sem letras maiusculas e sem pontuação.
    Parametro de entrada: string
    Valor de Saída: list
    """
    f9=str.split(f8)
    f10=f9[::-1] 
    f11=str(f10).strip('[]') 
    f12=f11.replace(",","") 
    f13=f12.replace("'","")
    return f13