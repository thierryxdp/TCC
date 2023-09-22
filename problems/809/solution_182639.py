def intercala(lista1, lista2):  
    c=lista2*2
    c[1::2]=lista2
    c[::2]=blista1
    return c