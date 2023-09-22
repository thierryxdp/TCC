# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas:list,H:int,L:int)->bool:
    """Diz se um colchão com dimensões A, B, C sendo  A<B<C passa por uma porta de altura H e largura L"""
        return int(medidas[1] or medidas[0]) <= max(H,L):