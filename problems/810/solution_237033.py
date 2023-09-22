def inverte(frase):
    """Dada uma frase, retorna a mesma frase sem pontuacao e com a ordem das palavras invertida, tudo em letra minuscula"""
    """entrada:str
    saida:str"""
    
    frase = str.replace(frase,"-"," ")
    frase = str.replace(frase,","," ")
    frase = str.replace(frase,":"," ")
    frase = str.replace(frase,";"," ")
    frase = str.replace(frase,"."," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    frase = str.lower(frase)
    frase = str.split(frase)
    frase = frase[::-1]
    
       
    return str.join(" ",frase)