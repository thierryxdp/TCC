# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """ dada uma lista com medidas de um colchao e dois valores inteiros medidas de uma porta, retorna um booleano caso o colhão passe pela porta"""
    medidasqueeuquero = medidas[1:]
    return min(medidasqueeuquero) <= H