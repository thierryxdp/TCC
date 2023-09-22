def ligua_p(palavra):
    '''traduz uma palavra em portugues para a ligua p
    str -> str'''
    
    palavra=str.lower(palavra)
    a=[a,e,i,o,u]
    
    for i in a:
        palavra=str.replace(palavra, i, i+'p'+i)
        
    return palavra