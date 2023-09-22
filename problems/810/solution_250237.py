def inverte(frase):
	"""
    Essa função inverte uma frase, contendo as mesmas palavras,
    porém em uma ordem inversa, sem letras maiusculas e sem pontuação.
    Parametro de entrada: string
    Valor de Saída: list
    """
    f1=frase.replace("-"," ")
    f2=f1.replace(","," ")
    f3=f2.replace(":"," ")
    f4=f3.replace(";"," ")
    f5=f4.replace("."," ")
    f6=f5.replace("?"," ")
    f7=f6.replace("!"," ")
    f8=f7.lower() 
    f9=str.split(f8)
    f10=f9[::-1] 
    f11=str(f10).strip('[]') 
    f12=f11.replace(",","") 
    f13=f12.replace("'","")
    return f13