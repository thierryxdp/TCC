def posLetra(frase,letra,n):
    """retorna em qual posicao esta a letra que 
    teve a ocorrencia n na frase)
    str,str,int -> int"""
    passador = 0
    juntador_de_ocorrencias = ()
    contador = len(juntador_de_ocorrencias)
    pegador = contador[n-1]
    while passador < len(frase):
        if letra in frase:
            juntador_de_ocorrencias += (frase.index(letra),)
   		    passador += 1
    return pegador
	if letra not in frase:
        return -1