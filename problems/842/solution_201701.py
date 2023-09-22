def pontos_por_time(ListaCAMP):
    '''calcula dicionário dos pontos de um time
    list[str,str,[int,int]],list[str,str,[int,int]]->
    dict{str:int,str:int}'''
    
    L1Placar=[w,x]
    L1=["a","b",L1Placar]
    L2Placar=[y,z]
    L2=["b","a",L2Placar]
    ListaCAMP={"a":str(x+y),"b":str(w+z)}
    
    return ListaCAMP