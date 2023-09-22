def pontos_por_time(jogoida,jogovolta):
    '''funcao que recebe duas listas como entrada e retorna um dicionario com o nome dos times e 
    seus pontos nas fases de ida e volta. entrada: lista, lista; saida: dicionario'''
    pontos = {,}
    if jogoida[3][1] > jogoida[3][2]:
        pontos[jogoida[1]] = 3
    if jogoida[3][1] < jogoida[3][2]:
        pontos[jogoida[2]] = 3
    if jogoida[3][1] == jogoida[3][2]:
        pontos[jogoida[1]] = 1 and pontos[jogoida[2]] = 1