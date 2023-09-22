def inverte(frase):
    '''funçao que dada uma frase inverte a ordem das palavras desta frase'''
    att1 = frase.replace("."," ")
    att2 = att1.replace("-"," ")
    att3 = att2.replace(","," ")
    att4 = att3.replace(":"," ")
    att5 = att4.replace(";"," ")
    att6 = att5.replace("!"," ")
    att7 = att6.replace("?"," ")
    att8 = att7.lower()
    att9 = att8.split()
    att10 = att9[::-1]
    att11 = str.join(" ",att10)
    return att11