def pontos_por_time(l1):
    '''Funcao que recebe uma lista com dois elementos, sendo a
    prima as informacoes do jogo de ida e a segunda com as informacoes
    do jogo de volta no modelo 'time da casa','time visitante',
    ['gols time da casa', 'gols time visitante'] e retorna um
    dicionario com o numero total de pontos dos times.
    Parametros:
    list
    Saida: dict'''
    p1 = 0
    p2 = 0
    
    if l1[2[0]] >l1[2[1]]:
        p1 = p1 + 3
    if l1[2[0]] <l1[2[1]]:
        p2 = p2 + 3
    if l1[2[0]] ==l1[2[1]]:
        p1 = p1 + 1
        p2 = p2 + 1
    if l1[-1[0]] >l1[-1[1]]:
        p2 = p2 + 3
    if l1[-1[0]] <l1[-1[1]]:
        p1 = p1 + 3
    if l1[-1[0]] ==l1[-1[1]]:
        p2 = p2 + 1
        p1 = p1 + 1
        
        
    d= {l1[0]:p1,l1[1]:p2}
    
    return d