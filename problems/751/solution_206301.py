# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Essa função irá retornar o número de palavras de uma deterninada frase ; string -> int"""
    if str.count(frase," ",0,-1) ==0 or str.count(frase," ",0,-1) > 0:
        return str.count(frase,' ', 0,-1) + 1