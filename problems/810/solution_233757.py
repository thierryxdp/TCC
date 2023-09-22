def inverte(frase):
    """essa função inverte a frase dada, tirando sua pontuação e mudando todas
    as letras para o minusculo
    str-->str"""
    frase=str.replace(frase,"-"," ")
    frase=str.replace(frase,","," ")
    frase=str.replace(frase,":"," ")
    frase=str.replace(frase,";"," ")
    frase=str.replace(frase,"?"," ")
    frase=str.replace(frase,"!"," ")
    frase=str.replace(frase,"."," ")
    frase=str.lower(frase)
    frase=str.split(frase)
    return frase[-1::-1]