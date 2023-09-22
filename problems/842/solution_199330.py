def pontos_por_time(lista):
    '''Docs.
    list, list -> dict '''

    lista = [jogo_ida, jogo_volta]
    jogo_ida = [str(jogo_ida[0]), str(jogo_ida[1])] + [a]
    jogo_volta = [str(jogo_volta[0]), str(jogo_volta[1])] + [b]

    #Gols que os times marcaram
    a = [c, d]
    b = [e, f]
    
    
    if a[0] > a[1] and b[1] > b[0]:
        return {str(jogo_volta[0]): 0, str(jogo_volta[1]): 6}
    elif a[1] > a[0] and b[0] > b[1]:
        return {str(jogo_volta[0]): 6, str(jogo_volta[1]): 0}
    elif a[0] == a[1] and b[0] == b[1]:
        return {str(jogo_volta[0]): 2, str(jogo_volta[1]): 2} 
    elif a[0] > a[1] and b[1] < b[0]:
        return {str(jogo_volta[0]): 3, str(jogo_volta[1]): 3} 
    elif a[1] > a[0] and b[1] > b[0]:
        return {str(jogo_volta[0]): 3, str(jogo_volta[1]): 3} 
    elif a[0] > a[1] and b[0] == b[1]:
        return {str(jogo_volta[0]): 1, str(jogo_volta[1]): 4} 
    elif a[0] < a[1] and b[0] == b[1]:
        return {str(jogo_volta[0]): 4, str(jogo_volta[1]): 1} 
    elif a[0] == a[1] and b[1] > b[0]:
        return {str(jogo_volta[0]): 1, str(jogo_volta[1]): 4}
    elif a[1] == a[0] and b[0] > b[1]:
        return {str(jogo_volta[0]): 4, str(jogo_volta[1]): 1}