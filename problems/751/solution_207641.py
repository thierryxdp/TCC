def quant_palavras(frase):
    ''' Função que dada uma string (frase) que represente uma frase
    qualquer, retorna o número de palavras que tal frase possui.
    Entrada: str
    Retorno: int '''
    
    lista_palavras = str.split(frase)
    numero_palavras = len(lista_palavras)
    
    return numero_palavras