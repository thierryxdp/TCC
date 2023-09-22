def inverte(x):
    """Função que dada uma frase retorna uma outra frase que 
    contenha as mesmas palavras da frase de entradana ordem
    inversa, sem letras maisculas e sem pontuação
    str-> str"""
    if "!" in x:
        x=str.replace(x,"!"," ")
    
    if "..." in x:
        x=str.replace(x,"..."," ")
    
    if "?" in x:
        x=str.replace(x,"?"," ")
    
    if "." in x:
        x=str.replace(x,"."," ")

    if "-" in x:
        x=str.replace(x,"-"," ")

    if "," in x:
        x=str.replace(x,","," ")

    if ";" in x:
        x=str.replace(x,";"," ")

    if ":" in x:
        x=str.replace(x,":"," ")
     
    
    lista= (str.split((str.lower(x))," "))
    lista.reverse()
    frase=str.join("",lista)
    return frase