def quant_palavras(frase):
    """A função acima retorna quantas palavras há na frase dada como entrada.
       str -> int"""
    return len(str.split(frase))

#Teste 1:
#quant_palavras('Perdão pelo atraso na entrega da atividade!')--> 7

#Teste 2:
#quant_palavras(' Não vai mais se repetir... ')--> 5