def inverte(s):
    """Removemos primeiramente todos as pontuaçoes, apos isso colocamos
    todas as letras em minuscula, e somente depois disso poderemos separar
    inverter e entregar uma string ao contrario
    str-->str
    """ 
    
    u=0
    a=str.replace(s,"-"," ")
    b=str.replace(a,","," ")
    c=str.replace(b,":"," ")
    d=str.replace(c,";"," ")
    e=str.replace(d,"."," ")
    f=str.replace(e,"?"," ")
    g=str.replace(f,"!"," ")
    h=str.lower(g)
    i=h.split()
    j=i.reverse()
    
    for palavras in j:
        u+= palavras
    
    
    
    
    print (j)