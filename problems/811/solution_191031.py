# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    """função que diz se um colchão passará ou não pela porta de sua casa com medidas H e L,
    altura e largura.
    list, int, int -> bool"""
    Hc = medidas[1]
    Lc = medidas[2]
    if L < Lc and H < Hc:
        return False
    esle:
        return True