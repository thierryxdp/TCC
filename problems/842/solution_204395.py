def pontosTime(l):
    '''dada uma lista de tamanho 2 com  as informações dos nomes dos times e placares dos jogos de ida e volta, retorna um dicionário
    com o nome do time e o total de pontos da fase. list -> dict''' 
    x=0
    y=0
    if l[0][2][0]>l[0][2][1]:
        x= x+3
    if l[0][2][0]<l[0][2][1]:
        y= y+3
    if l[0][2][0]==l[0][2][1]:
        x= x+1
        y= y+1
    if l[1][2][0]>l[1][2][1]:
        y= y+3
    if l[1][2][0]<l[1][2][1]:
        x= x+3
    if l[1][2][0]==l[1][2][1]:
        x= x+1
        y= y+1
    return { l[0][0]:x , l[0][1]:y}