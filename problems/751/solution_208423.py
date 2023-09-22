def quant_palavras(frase):
    """Retorna o número de palavras de uma frase dada como entrada.
str -> int"""
    frase = str.split(frase)
    return len(frase)

#Casos de teste:
# quant_palavras("Meu nome é Júlia") == 4
# quant_palavras(" Oi, você é o João?") == 5
# quant_palavras("OK! ") == 1