def pontos_por_time(ListaT):
    '''calcula nºpontos de 2 times em jogod de ida e volta
    list(str,str,tup),list(str,str,tup)->dic{str:int,str:int}'''
    
    J1=ListaT[0]
    "T1"==J1[0]
    "T2"==J1[1]
    PJ1=J1[2]
    
    J2=ListaT[1]
    "T1"==J2[1]
    "T2"==J2[0]
    PJ2=J2[2]
    
    ListaT=[J1,J2]
    
    if PJ1[0]>PJ1[1] and PJ2[1]>PJ2[0]:
        return {"T1":6,"T2":0}
    elif PJ1[0]>PJ1[1] and PJ2[1]==PJ2[0] or PJ1[0]==PJ1[1] and PJ2[1]>PJ2[0]:
        return {"T1":4,"T2":1}
    elif PJ1[0]==PJ1[1] and PJ2[1]==PJ2[0]:
        return {"T1":2,"T2":2}
    elif PJ1[0]>PJ1[1] and PJ2[1]<PJ2[0] or PJ1[0]<PJ1[1] and PJ2[1]>PJ2[0]:
        return {"T1":3,"T2":3}
    elif PJ1[0]<PJ1[1] and PJ2[1]==PJ2[0] or PJ1[0]==PJ1[1] and PJ2[1]<PJ2[0]:
        return {"T1":1,"T2":4}
    elif PJ1[0]<PJ1[1] and PJ2[1]<PJ2[0]:
        return {"T1":0,"T2":6}