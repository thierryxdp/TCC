# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def colchao(medidas,H,L):
    #A minha função colchão recebe como entrada uma lista (medidas, contendo as dimensoes do colchao), a altura e a largura da porta
    #Através de uma série de ifs, a função testa todas as combinações possíveis em que o colchão poderia atravessar a porta, testando as
    #diferentes combinações possíveis do eixo x, y e z
    atravessa = False

    if(medidas[0]<=H) and (medidas[1]<=L) or (medidas[0]<=L) and (medidas[1]<=H):
        atravessa = True
    if(medidas[1]<=H) and (medidas[0]<=L) or (medidas[1]<=L) and (medidas[0]<=H):
        atravessa = True
    if(medidas[0]<=H) and (medidas[2]<=L) or (medidas[0]<=L) and (medidas[2]<=H):
        atravessa = True
    if(medidas[2]<=H) and (medidas[0]<=L) or (medidas[2]<=H) and (medidas[0]<=L):
        atravessa = True
    if(medidas[1]<=H) and (medidas[2]<=L) or (medidas[1]<=H) and (medidas[2]<=L):
        atravessa = True
    if(medidas[2]<=H) and (medidas[1]<=L) or (medidas[2]<=H) and (medidas[1]<=L):
        atravessa = True

    return atravessa