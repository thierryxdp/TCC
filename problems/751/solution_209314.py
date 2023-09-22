def quant_palavras(frase):
    """Dada uma frase como entrada, a função retornará o número de
    palavras na frase.
    str -> int"""
    
    semespaco = str.strip(frase)
    
    separacao = str.split(semespaco)
    
    return len(separacao)