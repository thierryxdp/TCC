def quant_palavras(frase):
    """Função que recebe uma frase e retorna o número
    de palavras dessa frase
    str->int
    """
    frase = frase.replace(',','')
    frase = frase.replace('.','')
    frase = frase.replace(';','')
    frase = frase.replace(';','')
    
    return len(frase.split(' '))