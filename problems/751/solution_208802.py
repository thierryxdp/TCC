def quant_palavras(frase):
    "dada uma frase, retorna o numero total de letras str -> int"
    return len(frase) - str.count(frase, ' ') - str.count(frase, ',')