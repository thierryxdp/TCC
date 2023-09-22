def inverte(frase):
    """função que dada uma frase retorna outra fase em ordem invertida"""
    frase_saida=[]
    frase = str.replace(frase, "-", " ")
    frase = str.replace(frase, ":", " ")
    frase = str.replace(frase, ".", " ")
    frase = str.replace(frase, ",", " ")
    frase = str.replace(frase, ";", " ")
    frase = str.replace(frase, "!", " ")
    frase = str.replace(frase, "?", " ")
    frase = str.replace(frase, "...", " ")
    str.lower(frase)
    
    frase_entrada=str.split(frase)
    frase_entrada.reverse()
    frase_saida=str.join(" ",frase_entrada)
    return(frase_saida)