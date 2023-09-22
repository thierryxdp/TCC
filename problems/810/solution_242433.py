def inverte(frase):
    
    frase = str.replace(frase,".","")
    
    frase = str.replace(frase,"-","")
    
    frase = str.replace(frase,",","")
    
    frase = str.replace(frase,":","")
    
    frase = str.replace(frase,";","")
    
    frase = str.replace(frase,"!","")
    
    frase = str.replace(frase,"?","")
    

    frase = str.lower(frase)

    lista = str.split(frase," ")

    list.reverse(lista)

    frase = " ".join(lista)
    
    return frase