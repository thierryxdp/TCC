def pontos_por_time(jogos):
    '''Dado  os placares dos jogos de ida e volta, a funcao retorna a pontuacao de cada um dos dois times dado na lista
       sendo vitoria=3pts e empate=1pt.
       list->dic'''
    jogoida = jogos[0]
    jogovolta = jogos[1]
    ptst1 = []
    ptst2 = []
    if jogoida[2][0]>jogoida[2][1]:
        pts1 = [3,0]
    if jogoida[2][0]==jogoida[2][1]:
        pts1 = [1,1]
    if jogoida[2][0]<jogoida[2][1]:
        pts1 = [0,3]
    if jogovolta[2][0]>jogovolta[2][1]:
        pts2 = [3,0]
    if jogovolta[2][0]==jogovolta[3][1]:
        pts2 = [1,1]
    if jogovolta[2][0]<jogovolta[3][1]:
        pts2 = [0,3]
    soma_pontos = (pts1[0]+pts2[1]),(pts1[1]+pts2[0])
    resultado = {jogoida[0]:soma_pontos[0], jogovolta[0]:soma_pontos[1]}