def posLetra(frase,letra,numero):
    '''' que recebe uma 2 string e um numreo e trornaa um numero; str,str,int-> int'''
    if frase.index(letra)< numero:
        return frase.index(letra)
    
    if numero==1:
        return frase.index(letra)
    
    elif frase.index(letra)>0:
        return -1