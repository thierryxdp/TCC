def inverte(frase):
    frase=str.replace(frase,";","")
    frase=str.replace(frase,"-","")
    frase=str.replace(frase,"!","")
    frase=str.replace(frase,";","")
    frase=str.replace(frase,"?","")
    frase=str.replace(frase,",","")
    frase=str.replace(frase,":","")
    frase=str.replace(frase,".","")
    
    frase_2=str.lower(frase)
    lista=str.split(frase_2,' ')
    lista_2=lista[::-1]
    return str.join(" ",lista_2)