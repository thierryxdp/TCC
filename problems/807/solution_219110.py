def conta_frases (frase):
    '''funcao que dado um texto,conta o numero de frases que contem no texto'''
    
    novafrase =  str.replace(frase,";"," ")
    novafrase = str.replace(frase,"." ," ")
    novafrase = str.replace(frase,":"," ")
    novafrase = str.replace(frase," ?"," ")
    novafrase = str.replace(frase,","," ")
    novafrase = str.replace(frase,"!"," ")
    novafrase = str.replace(frase,"-"," ")
    return novafrase