def intercala(lista1,lista2):
    'Função que intercala duas listas'
    
    z=[",",",",","]
    x=lista1
    y=lista2
    
    z[0]=x[0]
    z[1]=y[0]
    z[2]=x[1]
    z[3]=y[1]
    z[4]=x[2]
    z[5]=y[2]
    
    return z