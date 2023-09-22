# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    """
    Essa função recebe as medidas de um colchão em uma lista, 
    a altura e a largura da porta de João, e assim retorna se 
    o colchão passa ou não pela porta;
    list, int, int -> bool
    """
    if medidas[1] <= L or medidas[1] <= H:
        return True
    if medidas[2] <= H or medidas[2] <= L:
        return True
    return False