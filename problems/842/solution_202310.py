#Start your python function here

def pontos_por_time(lista):
    resultado_ida = lista[0][2]
    resultado_volta = lista[1][2]
    dic_res = {lista[0][0]: 0, lista[0][1]: 0}
    
    if(resultado_ida[0] > resultado_ida[1]):
           dic_res[lista[0][0]] += 3
    elif(resultado_ida[0] < resultado_ida[1]):
            dic_res[lista[0][1]] += 3
    else:
       dic_res[lista[0][0]] += 1
       dic_res[lista[0][1]] += 1
       
    if(resultado_volta[0] > resultado_volta[1]):
           dic_res[lista[1][0]] += 3
    elif(resultado_volta[0] < resultado_volta[1]):
            dic_res[lista[1][1]] += 3
    else:
       dic_res[lista[1][0]] += 1
       dic_res[lista[1][1]] += 1

    return dic_res