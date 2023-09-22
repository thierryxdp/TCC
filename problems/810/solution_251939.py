def inverte(frase):
    pts = str.split(frase,".")
    text1 = " ".join(pts)
    
    virg = str.split(text1,",")
    text2 = " ".join(virg)
    
    excl = str.split(text2,"!")
    text3 = " ".join(virg)
    
    inte = str.split(text3,"?")
    text4 = " ".join(excl)
    
    trav = str.split(text4,"-")
    text5 = " ".join(trav)
    
    dois_pts = str.split(text5,":")
    text6 = " ".join(dois_pts)
    
    pts_virg = str.split(text6,";")
    text7 = " ".join(pts_virg)
    
    lista_frase = str.split(text7)
    list.reverse(lista_frase)
    frase_invertida = " ".join(lista_frase)
    
    return str.lower(frase_invertida)