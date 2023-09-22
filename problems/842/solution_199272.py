def pontos_por_time(lista):
    
    lista0=lista[0]
    lista1=lista[1]
    
    sublista0=lista0[2]
    sublista1=lista1[2]
    
if sublista0[0]>sublista0[1] and sublista1[0]<sublista1[1]:
    x=6
    y=0
    
if sublista0[0]>sublista0[1] and sublista1[0]==sublista1[1]:
    x=4
    y=1
    
if sublista0[0]==sublista0[1] and sublista1[0]<sublista1[1]:
    x=4
    y=1
    
if sublista0[0]==sublista0[1] and sublista1[0]==sublista1[1]:
    x=2
    y=2
    
if sublista0[0]>sublista0[1] and sublista1[0]>sublista1[1]:
    x=3
    y=3
    
if sublista0[0]<sublista0[1] and sublista1[0]<sublista1[1]:
    x=3
    y=3
    
if sublista0[0]<sublista0[1] and sublista1[0]==sublista1[1]:
    x=1
    y=4
    
if sublista0[0]==sublista0[1] and sublista1[0]>sublista1[1]:
    x=1
    y=4
    
else:   
    x=0
    y=6
    
dicio={lista0[0]:x,lista0[1]:y}

return dicio