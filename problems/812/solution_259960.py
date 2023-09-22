def retira_pontuacao (frase: str) -> str:
    '''Recebe uma frase e retorna essa mesma frase sem qualquer pontuação'''
    
    fraseA = frase
    
    fraseA = fraseA.replace("...", " ")
    fraseA = fraseA.replace("!", " ")
    fraseA = fraseA.replace("?", " ")
    fraseA = fraseA.replace(".", " ")
    fraseA = fraseA.replace("-", " ")
    fraseA = fraseA.replace(",", " ")
    fraseA = fraseA.replace(";", " ")
    fraseA = fraseA.replace(":", " ")
    
    return fraseA