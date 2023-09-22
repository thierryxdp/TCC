def quant_palavras(frase:str)->int :
    "recebe uma frase e retorna o número de palavrase da mesma"
    quantPalavras = len(str.split(frase,' '))
    return quantPalavras