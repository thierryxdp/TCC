# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    """Retorna se o colchão passa ou não pela porta
       Entrada: list, int, int
       Saida: bool
    """
    if medidas[1]>H:
        return False
    if medidas[1]<H:
        return True