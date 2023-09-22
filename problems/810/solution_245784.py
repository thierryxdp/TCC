def inverterFrase(frase):
    x=0
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
    retrn(frase_saida)