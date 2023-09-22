def pontos_por_time(lista):
    """Retorna um dicionário contendo chaves sendo os nomes dos times e os valores
    os totais de pontos de cada time a partir dos placares dos jogos dados como entrada 
x= pontos do time presente em lista[0][0]
y= pontos do time presente em lista[0][1]
    list -> dict"""
    x=0
    y=0
    if lista[0][2][0]>lista[0][2][1]:
        x+=3
        y+=0
    if lista[0][2][0]<lista[0][2][1]:
        y+=3
        x+=0
    if lista[1][2][0]>lista[1][2][1]:
        y+=3
        x+=0
    if lista[1][2][0]<lista[1][2][1]:
        x+=3
        y+=0
    if lista[0][2][0]==lista[0][2][1]:
        y+=1
        x+=1
    if lista[1][2][0]==lista[1][2][1]:
        y+=1
        x+=1
    return {str(lista[0][0]):x,str(lista[0][1]):y}