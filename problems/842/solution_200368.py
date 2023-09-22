def pontos_por_time(jogos):
    '''funcao que recebe duas listas como entrada e retorna um dicionario com o nome dos times e 
    seus pontos nas fases de ida e volta. entrada: lista, lista; saida: dicionario'''
    pontos = {}
    if jogos[0][2][0] > jogos[0][2][1]:
        pontos[jogos[0][0]] = 3
        pontos[jogos[0][1]] = 0
    if jogos[0][2][0] < jogos[0][2][1]:
        pontos[jogos[0][1]] = 3
        pontos[jogos[0][0]] = 0
    if jogos[0][2][0] == jogos[0][2][1]:
        pontos[jogos[0][0]] = 1
        pontos[jogos[0][1]] = 1
    if jogos[1][2][1] > jogos[1][2][0]:
        pontos[jogos[0][0]] = pontos[jogos[0][0]] + 3
        pontos[jogos[0][1]] = pontos[jogos[0][1]]
    if jogos[1][2][1] < jogos[1][2][0]:
        pontos[jogos[0][1]] = pontos[jogos[0][1]] + 3
        pontos[jogos[0][0]] = pontos[jogos[0][0]]
    if jogos[1][2][1] == jogos[1][2][0]:
        pontos[jogos[0][1]] = pontos[jogos[0][1]] + 1
        pontos[jogos[0][0]] = pontos[jogos[0][0]] + 1
    return pontos