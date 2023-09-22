def quant_palavras(frase):
    """Função que recebe uma frase e retorna o número de palavras
       contida na mesma
       str -> int"""
    dividir_frase= str.split(frase)
    return len(dividir_frase)