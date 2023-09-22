def pontos_por_time(jogoida,jogovolta):
    '''funcao que recebe duas listas como entrada e retorna um dicionario com o nome dos times e 
    seus pontos nas fases de ida e volta. entrada: lista, lista; saida: dicionario'''
    pontos = {}
    if jogoida[2][0] > jogoida[2][1]:
        pontos[jogoida[0]] = 3
    if jogoida[2[0] < jogoida[2[1]:
        pontos[jogoida[1]] = 3
    if jogoida[2[0] == jogoida[2[1]:
        pontos[jogoida[0]] = 1 and pontos[jogoida[1]] = 1
    if jogovolta[2][1] > jogovolta[2][0]:
        pontos[jogoida[0]] = pontos[jogoida[0]] + 3
    if jogovolta[2][1] < jogovolta[2][0]:
        pontos[jogoida[1]] = pontos[jogoida[1]] + 3
    if jogovolta[2][1] == jogovolta[2][0]:
        pontos[jogoida[1]] = pontos[jogoida[1]] + 1 and pontos[jogoida[0]] = pontos[jogoida[0]] + 1