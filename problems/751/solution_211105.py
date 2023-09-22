def quant_palavras(frase):
  # a função split quebra a frase com base nos espaços e unifica as palavras.
  # a função len conta as unificações feitas pelo split.
    frase = str.split(frase)
    return len(frase)