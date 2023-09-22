"""A função quant_palavras tem como objetivo calcular o número de palavras 
contidas numa frase, desconsiderando os espaços e as pontuações; tudo por
meio da junção das funções len e split."""

def quant_palavras(frase):
    return len(str.split(frase))