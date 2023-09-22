# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """ Verifica se o colchao com as dimenões fornecidas passa pela porta.
    	entrada: lista e 2 int -> saida:boleao, retorna true caso o colchão passe."""
    return ((medida[0] < H and medida[1] < L ) or (medida[0] < H and medida[2] < L ) or (medida[1] < H and medida[0] < L ) or (medida[1] < H and medida[2] < L ) or (medida[2] < H and medida[0] < L ))or (medida[2] < H and medida[1] < L )