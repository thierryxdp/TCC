def pontos_por_time(lista):
    """Calcula e retorna o total de pontos de uma fase de jogo de futebol, onde a a variavel de entrada(lista)é do tipo lista e eh formada por duas listas, uma com duas strings
representando os nomes dos times mais uma lista interna com o numero de gols respectivamente de cada time e a outra lista com o mesmo formato só que com os dados da outra partida;
list --> dicionario"""
        
    if lista[0][2][0]> lista[0][2][1] and lista[1][2][1]>lista[1][2][1]:
        return {lista[0][0]:6, lista[0][1]:0}
    elif lista[0][2][0]== lista[0][2][1] and  lista[1][2][1]== lista[1][2][0]:
        return {lista[0][0]:2,lista[0][1]:2}
    elif lista[0][2][0]< lista[0][2][1] and lista[1][2][1]>lista[1][2][0]:
        return {lista[0][0]:3, lista[0][1]:3}
    elif lista [0][2][0]<lista[0][2][1] and lista[1][2][1]>lista[1][2][0]:
        return {lista[0][0]:6, lista[0][1]:0}
    else:
        return {lista[0][0]:0, lista[0][1]:6}