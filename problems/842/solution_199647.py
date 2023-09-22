def pontos_por_time(lista):
    """A função retorna um dicionário cujos mapeamentos são:<nome do time> --> <números de pontos>
    recebendo uma lista com dois elementos como entrada.
    list-->dict."""
    ida, volta = lista[0],lista[1]
    dic = {ida[0]:0, ida{1}:0}
    if ida[2][0] > ida[2][1]:
        dic[ida[0]]= dic[ida[0]] + 3
    if ida[2][1] > ida[2][0]:
        dic[ida[1]]= dic[ida[1]] + 3
    if ida[2][1]== ida[2][0]:
        dic[ida[1]]= dic[ida[1]] + 1
        dic[ida[0]]= dic[ida[0]] + 1
    if volta[2][0]> volta[2][1]:
        dic[ida[1]]= dic[ida[1]] + 3
    if volta[2][1]>volta[2][0]:
        dic[ida[0]]= dic[ida[0]] + 3
    if volta[2][1]==volta[2][0]:
        dic[ida[1]]= dic[ida[1]] + 1
        dic[ida[0]]= dic[ida[1]] + 1