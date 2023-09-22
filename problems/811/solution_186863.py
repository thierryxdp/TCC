# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas:list, H:int, L:int)->bool:
    if (medidas[0] =< H and medidas[1] =< L) or (medidas[0] =< L and medidas[1] =< H):
        return True
    return False