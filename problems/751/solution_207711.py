# string -> int
def quant_palavras(frase):
    """A partir da frase dada, contamos o numero de intervalo entre as 		
    	palavras para assim saber quando uma palavra acaba, logo		
        descobrimos o numero de palavras na frase"""
    z= (frase.count(".")+frase.count("?")+frase.count("!"))- 2*frase.count("...") + frase.count(" ")
    return z