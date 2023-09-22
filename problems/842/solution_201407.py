def pontos_por_time(lista):
    """Funcao que recebe como entrada uma lista de 2 elementos, e cada elemento
    e uma lista, e retorna um dicionario com os pontos de cada time.
    list->dict"""
    lista=[[time1,time2,[golida1,golida2]],[time2,time1,[golvolta2,golvolta1]]]
    if golida1>golida2 and golvolta1>golvolta2:
        return {time1:'6',time2:'0'}
    elif golida1>golida2 and golvolta1<golvolta2:
        return {time1:'3',time2:'3'}
    elif golida1>golida2 and golvolta1==golvolta2:
        return {time1:'4',time2:'1'}
    elif golida1==golida2 and golvolta1==golvolta2:
        return {time1:'2',time2:'2'}
    elif golida1<golida2 and golvolta1>golvolta2:
        return {time1:'3',time2:'3'}
    elif golida1<golida2 and golvolta1<golvolta2:
        return {time1:'0',time2:'6'}
    elif golida1<golida2 and golvolta1==golvolta2
    	return {time1:'1',time2:'4'}
    elif golida1==golida2 and golvolta1<golvolta2:
        return {time1:'1',time2:'4'}
    elif golida1==golida2 and golvolta1>golvolta2:
        return {time1:'4',time2:'1'}