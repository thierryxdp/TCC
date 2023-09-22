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
    #[['a','b',[2,1]],['b','a',[1,2]]]
    l2 = l1[0]
    r1 = l2[2]
    l3 = l1[1]
    r2 = l3[2]
    if r1[0] >r1[1]:
        p1 = p1 + 3
    if r1[0] <r1[1]:
        p2 = p2 + 3
    if r1[0] ==r1[1]:
        p1 = p1 + 1
        p2 = p2 + 1
    if r2[0] >r2[1]:
        p2 = p2 + 3
    if r2[0] <r2[1]:
        p1 = p1 + 3
    if r2[0] ==r2[1]:
        p2 = p2 + 1
        p1 = p1 + 1
        
        
    d= {l2[0]:p1,l2[1]:p2}
    
    return d