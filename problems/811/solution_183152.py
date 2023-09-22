# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    """Função para calcular se um colchão passa por uma porta.
       Onde: "medidas" - é uma lista com as medidas do colçhão;
             "H" - é a altura da porta;
             "L" - é a largura da porta.
    list, int, int -> bool"""
    if medidas[2] <= H or medidas[1] <= L or medidas[2] <= L or medidas[1] <= H:
        teste = True
    else:
        teste = False
    return teste