def pontos_por_time(JogoIda,JogoVolta):
    '''calcula número pontos por time em 2 jogos
    list(str,str,tup)+list(str,str,tup)->
    dic{str:int,str:int}'''
    
    len(JogoIda)==3
    Time1=JogoIda[0]
    
    len(JogoVolta)==3
    Time2=JogoVolta[0]
    
    if "JogoIda[2][0]">"JogoIda[2][1]" and "JogoVolta[2][1]">"JogoVolta[2][0]":
        return {Time1:6,Time2:0}
    elif ["JogoIda[2][0]">"JogoIda[2][1]" and "JogoVolta[2][1]"="JogoVolta[2][0]"]or["JogoIda[2][0]"="JogoIda[2][1]" and "JogoVolta[2][1]">"JogoVolta[2][0]"]:
            return {Time1:4,Time2:1}
    elif "JogoIda[2][0]"="JogoIda[2][1]" and "JogoVolta[2][1]"="JogoVolta[2][0]":
            return {Time1:2,Time2:2}
    elif ["JogoIda[2][0]">"JogoIda[2][1]" and "JogoVolta[2][1]"<"JogoVolta[2][0]"]or["JogoIda[2][0]"<"JogoIda[2][1]" and "JogoVolta[2][1]">"JogoVolta[2][0]"]:
            return {Time1:3,Time2:3}
    elif ["JogoIda[2][0]"<"JogoIda[2][1]" and "JogoVolta[2][1]"="JogoVolta[2][0]"]or["JogoIda[2][0]"="JogoIda[2][1]" and "JogoVolta[2][1]"<"JogoVolta[2][0]"]:
            return {Time1:1,Time2:4}
    elif "JogoIda[2][0]"<"JogoIda[2][1]" and "JogoVolta[2][1]"<"JogoVolta[2][0]":
            return {Time1:0,Time2:6}