def pontos_por_time(list_um,list_dois):
    """xxxxxxxxxxxx"""
    
   
    gols_um = [n1,n2]
    gols_dois = [n3,n4]
    
    list_um = [x1, x2, gols_um]
    list_dois = [x2, x1, gols_dois]
    
    if gols_um[0]>gols_um[1] and gols_dois[1]>gols_dois[0]:
        return {str(x1):6, str(x2):0}
    if (gols_um[0]>gols_um[1] and gols_dois[1]==gols_dois[0]) or (gols_um[0]==gols_um[1] and gols_dois[1]>gols_dois[0]):
        return {str(x1):4, str(x2):1}
    if (gols_um[0]>gols_um[1] and gols_dois[1]<gols_dois[0]) or (gols_um[0]<gols_um[1] and gols_dois[1]>gols_dois[0]):
        return {str(x1):3, str(x2):3}
    if gols_um[0]==gols_um[1] and gols_dois[1]==gols_dois[0]:
        return {str(x1):2, str(x2):2}
    if  gols_um[0]<gols_um[1] and gols_dois[1]<gols_dois[0]:
        return {str(x1):0, str(x2):6}
    if  (gols_um[0]<gols_um[1] and gols_dois[1]==gols_dois[0]) or (gols_um[0]==gols_um[1] and gols_dois[1]<gols_dois[0]):
        return {str(x1):1, str(x2):4}