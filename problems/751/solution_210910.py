def quant_palavras(frase):
    """Retornar uma função que dada uma frase, retorne o n° de palavras da mesma;str=>int"""
	p1=(str.strip(frase))
    return (len(str.split(frase, " " )))