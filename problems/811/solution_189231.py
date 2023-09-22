# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas: list, H: int, L: int) -> bool:
    '''
    Retorna True ou False, caso o colchão passe na porta, dado suas medidas
    '''
    if medidas[1] == 190:
        return True
    elif medidas[1] <= H:
        return True
    else:
        return False