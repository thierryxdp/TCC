def quant_palavras(frase):
     """Contabiliza o numero de palavras da frase escolhida, ja descartando os separadores
Assinatura: str -> int"""
    
    result = len(frase.split())

    print(str(result))