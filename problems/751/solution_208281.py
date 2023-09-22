def quant_palavras(frase):
    """Essa função retorna o número de palavras dada uma frase, considerando a possibilidade de ter espaços no inicío e no fim"""
    #A função strip retira os possíveis espaços do início e do final da frase e a função count conta cada espaço entre as palavras de uma frase dada e soma 1 unidade para retornar o número de palavras
    #string->int
    f=str.strip(frase)
    return str.count(f,' ')+1