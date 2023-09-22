def quant_palavras(frase):
    """Funcao que retorne a quantidades de palavras na frase
entrada: str
saida: int"""
    #frase = 'esqueci o isqueiro na esquina da escola'
    return len(frase.split())
    #resultado ['esqueci', 'o', 'isqueiro', 'na', 'esquina', 'da', 'escola']