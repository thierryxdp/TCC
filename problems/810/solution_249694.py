def inverte(frase):
    """Funcao que recebe uma frase como entrada e retorna a mesma de forma invertida e substituindo todos os caracteres por espaco
    str -> str"""
    fraseA = frase.replace(","," ")
    fraseB = fraseA.replace("?"," ")
    fraseC = fraseB.replace("."," ")
    fraseD = fraseC.replace("-"," ")
    fraseE = fraseD.replace("!"," ")
    fraseF = fraseE.replace(","," ")
    fraseG = fraseF.replace("."," ")
    fraseH = fraseG.lower()
    fraseI = fraseH.split(" ")
    fraseI.reverse()
    fraseJ ="".join(fraseI)
    return fraseJ