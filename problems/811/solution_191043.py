# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """Função que pegas os valores de entradas da medida do colchão e compara com a altura e largura da porta, retornado
    Verdadeiro se passa pela porta e Falso se não passa.
    int,int→bool"""   
    if medidas[1] > H and medidas[2] > L:
        return False
    else:
        return True