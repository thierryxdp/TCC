def pontos_por_time(lista):
    
    lista0=lista[0]
    lista1=lista[1]
    
    sublista0=lista0[2]
    sublista1=lista1[2]
    
    """"
    A primeira lista pode ser dividida em 2 listas,onde o termo [2]
    de cada uma eh outra lista, sendo assim foram dados os nomes de 
    lista e sublista. A sublista foi responsavel pelo placar, onde 
    foi possivel compara-los para se ter a pontuação de cada time
    
    """"
    
    
    
    if sublista0[0]>sublista0[1] and sublista1[1]>sublista1[0]:
        x=6
        y=0
    
    if sublista0[0]>sublista0[1] and sublista1[1]==sublista1[0]:
        x=4
        y=1
    
    if sublista0[0]==sublista0[1] and sublista1[1]>sublista1[0]:
        x=4
        y=1
    
    if sublista0[0]==sublista0[1] and sublista1[1]==sublista1[0]:
        x=2
        y=2
    
    if sublista0[0]>sublista0[1] and sublista1[1]<sublista1[0]:
        x=3
        y=3
    
    if sublista0[0]<sublista0[1] and sublista1[1]>sublista1[0]:
        x=3
        y=3
    
    if sublista0[0]<sublista0[1] and sublista1[1]==sublista1[0]:
        x=1
        y=4
    
    if sublista0[0]==sublista0[1] and sublista1[1]<sublista1[0]:
        x=1
        y=4
    
    if sublista0[0]<sublista0[1] and sublista1[1]<sublista1[0]:  
        x=0
        y=6
    
    dicio={lista1[1]:x,lista1[0]:y}

    return dicio