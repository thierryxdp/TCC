# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """ Verifica se o colchao com as dimenões fornecidas passa pela porta.
    	entrada: lista e 2 int -> saida:boleao, retorna true caso o colchão passe."""
    return ((medidas[0] < H and medidas[1] < L ) or (medidas[0] < H and medidas[2] < L ) or (medidas[1] < H and medidas[0] < L ) or (medidas[1] < H and medidas[2] < L ) or (medidas[2] < H and medidas[0] < L ))or (medidas[2] < H and medidas[1] < L )