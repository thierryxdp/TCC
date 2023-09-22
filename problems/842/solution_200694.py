def pontos_por_time(x):
   
    x1 = x[0]
    x2 = x[1]
    y1 = x1[2]
    y2 = x2[2]
    if str(x1[0]) == str(x2[0]):
        if y1[0] > y1[1] and y2[0] > y2[1]:
            return {x1[0] : 6, x1[1] : 0}
        elif y1[0] > y1[1] and y2[0] < y2[1]:
            return {x1[0] : 3, x1[1] : 3}
        elif y1[0] < y1[1] and y2[0] < y2[1]:
            return {x1[0] : 0, x1[1] : 6}
        elif y1[0] == y1[1] and y2[0] == y2[1]:
            return {x1[0] : 2, x1[1] : 2}
        elif y1[0] > y1[1] and y2[0] == y2[1]:
            return {x1[0] : 4, x1[1] : 1}
        elif y1[0] == y1[1] and y2[0] > y2[1]:
            return {x1[0] : 4, x1[1] : 1}
        elif y1[0] == y1[1] and y2[0] < y2[1]:
            return {x1[0] : 1, x1[1] : 4}
        elif y1[0] < y1[1] and y2[0] > y2[1]:
            return {x1[0] : 3, x1[1] : 3}
        elif y1[0] < y1[1] and y2[0] == y2[1]:
            return {x1[0] : 1, x1[1] : 4}
    elif str(x1[0]) != str(x2[0]):
        if y1[0] > y1[1] and y2[0] > y2[1]:
            return {x1[0] : 3, x1[1] : 3}
        elif y1[0] > y1[1] and y2[0] < y2[1]:
            return {x1[0] : 6, x1[1] : 0}
        elif y1[0] < y1[1] and y2[0] < y2[1]:
            return {x1[0] : 3, x1[1] : 3}
        elif y1[0] == y1[1] and y2[0] == y2[1]:
            return {x1[0] : 2, x1[1] : 2}
        elif y1[0] > y1[1] and y2[0] == y2[1]:
            return {x1[0] : 4, x1[1] : 1}
        elif y1[0] == y1[1] and y2[0] > y2[1]:
            return {x1[0] : 1, x1[1] : 4}
        elif y1[0] == y1[1] and y2[0] < y2[1]:
            return {x1[0] : 4, x1[1] : 1}
        elif y1[0] < y1[1] and y2[0] > y2[1]:
            return {x1[1] : 6, x1[0] : 0}
        elif y1[0] < y1[1] and y2[0] == y2[1]:
            return {x1[0] : 1, x1[1] : 4}