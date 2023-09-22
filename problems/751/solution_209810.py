# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    """ 
    string -> int
    a função tem como parâmetro de entrada uma frase que é uma string depois de separar as
    palavras com o split o len dará a sua quantidade de palavras que é o resultado que queremos.
    """
    result = len(frase.split())
    return result