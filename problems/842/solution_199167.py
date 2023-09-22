def pontos_por_time(lista):
    lista = [['time1','time2',[a,b]],['time1','time2',[c,d]]]
    dici = {lista[0][0]:0, lista[1][0]:1}
    if a>b and c>d:
        return dici['time1'] += 6
    elif a>b and c=d:
        return dici['time1'] += 4
    elif a=b and c<d:
        return dici['time1'] += 4
        if a<b and c<d:
            return dici['time2'] += 6
        elif a<b and c=d:
            return dici['time2'] += 4
        elif a=b and c<d:
            return dici['time2'] += 4
        
           else:
                return dici['time1'] +=2
                       dici['time2'] +=2