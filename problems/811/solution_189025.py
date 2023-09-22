# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas:list,H:int,L:int)->bool:
    if int(medidas[1])<=H and H>L:
        return True
    elif int(medidas[1])>H and H>L:
        return False
    elif int(medidas[0])<=L and H>L:
        return True
    elif int(medidas[0])>L and H>L:
        return False