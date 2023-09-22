def quant_palavras(frase):
    """função que conta palavras de uma frase.
    string -> int"""
    contagem = frase.split(" ") #Cria uma lista com os elementos de frase separados por espaço
                                #As palavras são separadas dessa forma
    
    return len(contagem) #retorna o tamanho da lista com as palavras