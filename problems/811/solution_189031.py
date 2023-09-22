# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas:list,H:int,L:int)->bool:
    if int(medidas[1] and medidas[0]) <= max(H,L):
        return True
    elif int(medidas[1] and medidas[0]) > max(H,L):
        return False