# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas:list,H:int,L:int)->bool:
    if int(medidas[1])<=H or L:
        return True
    elif int(medidas[1])>H or L:
        return False
    elif int(medidas[0])<=L or H:
        return True
    elif int(medidas[0])>L or H:
        return False