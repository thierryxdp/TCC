def pontos_por_time(listaIDA,listaVOLTA):
    """De acodo com as listas de entrada, retorne o time que mais obteve pontos"""
    golsIDA=listaIDA[2]
    golsvolta=listavolta[2]
    pontos={"listaIDA[0]":"pontuacaomandante","listaIDA[1]":"pontuacaovisitante"}
    if golsIDA[0]>golsIDA[1]: