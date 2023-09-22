def inverte(frase):
    """Esta é a função que dada uma frase retorna outra que contenha as mesmas palavras da frase original porém na ordem inversa, sem letras maiúsculas e sem pontuação"""
    frase1= str.replace(frase,",","")
    frase2= str.replace(frase1,".","")
    frase3= str.replace(frase2,"!","")
    frase4= str.replace(frase3,"...","")
    frase5= str.replace(frase4,"..","")
    frase6= str.replace(frase5,"?","")
    frase7= str.replace(frase6,"-","")
    frase8= str.replace(frase7,":","")
    frase9= str.replace(frase8,";","")
    frase10= str.lower(frase9)
    y= str.split(frase10," ") and str.split(frase10,"-")
    invertida= y[::-1]
    frase_final= " ".join(invertida)
    return frase_final