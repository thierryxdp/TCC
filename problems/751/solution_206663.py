def quant_palavras(frase):
    """ retorna o número de palavras da frase, incluindo espaços no início e no final"""
    
    if frase[-1]=='':
        frase=frase[:-2]
        frase=frase.split('')
        return len(frase)
    else:
        frase=frase.split('')
        return len(frase)