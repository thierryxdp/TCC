def retira_pontuacao(frase):
    """Funcao que retorna uma frase, naqual todos os seus caracteres foram substituidos por espaco
    str -> str"""
    fraseA = frase.replace(","," ")
    fraseB = fraseA.replace("?"," ")
    fraseC = fraseB.replace("."," ")
    fraseD = fraseC.replace("-"," ")
    fraseE = fraseD.replace("!"," ")
    fraseF = fraseE.replace(","," ")
    fraseG = fraseF.replace("."," ")
    return fraseG