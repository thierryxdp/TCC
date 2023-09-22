# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    '''
    recebe lista[int], int, int
    a função compara todas combinações de duas medidas e checa se
    existe o caso onde as duas medidas são menores que H e L respectivamente.
    retorna booleana
    '''
    passa = False #u shall not pass
    for i in range(3):
        for j in range(3):
            if medidas[i]<=H and medidas[j]<=L and i!=j:
                passa = True
    return passa