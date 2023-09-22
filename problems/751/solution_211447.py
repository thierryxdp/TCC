# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    def quant_palavras(frase):
        ''' funcao que recebe uma frase(s) e retorna o numero de palavras que nela há, str-->int'''
        lista = str.split(frase)
        return len(lista)