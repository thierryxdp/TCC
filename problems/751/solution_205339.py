def quant_palavras(frase:str)->int:
    
    
    """Função que dada uma frase, conta o número de palavras que ela tem,considerando espaços no incio e fim"""
    
    return len(str.split(frase))