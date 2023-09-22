def conta_frases(texto):
    """Funcao que conta o numero de frases que aparecem em um texto,
    cada frase termina em um ponto final, um ponto de exclamacao,
    ponto de interrogacao ou tres pontos em sequencia (reticencias);
    string -> int"""
  
    if str.find(texto,"?") != -1 and str.find((str.replace(texto,"...",".")),".") != -1 and str.find(texto,"...") != -1 and str.find(texto,"!") != -1:
        return str.count(texto,"?") + str.count((str.replace(texto,"...",".")),".") + str.count(texto,"!")
    
    elif str.find(texto,"?") != -1 and str.find((str.replace(texto,"...",".")),".") != -1 and str.find(texto,"...") != -1:
        return str.count(texto,"?") + str.count((str.replace(texto,"...",".")),".") 
    
    elif str.find(texto,"!") != -1 and str.find(texto,"?") != -1 and str.find(texto,"...") != -1:
        return str.count(texto,"!") + str.count(texto,"?") + str.count(texto,"...")

    elif str.find((str.replace(texto,"...",".")),".") != -1 and str.find(texto,"!") != -1 and str.find(texto,"...") != -1:
        return str.count((str.replace(texto,"...",".")),".") + str.count(texto,"!")  

    elif str.find(texto,".") != -1 and str.find(texto,"!") != -1 and str.find(texto,"?") != -1:
        return str.count(texto,".") + str.count(texto,"!") + str.count(texto,"?")
    
    elif str.find((str.replace(texto,"...",".")),".") != -1 and str.find(texto,"...") != -1:
        return str.count((str.replace(texto,"...",".")),".") 
      
    elif str.find(texto,"?") != -1 and str.find(texto,"...") != -1:
        return str.count(texto,"?") + str.count(texto,"...")

    elif str.find(texto,"!") != -1 and str.find(texto,"...") != -1:
        return str.count(texto,"!") + str.count(texto,"...")

    elif str.find(texto,"!") != -1 and str.find(texto,"?") != -1:
        return str.count(texto,"!") + str.count(texto,"?")  
    
    elif str.find(texto,".") != -1 and str.find(texto,"!") != -1:
        return str.count(texto,".") + str.count(texto,"!")
    
    elif str.find(texto,".") != -1 and str.find(texto,"?") != -1:
        return str.count(texto,".") + str.count(texto,"?")

    elif str.find(texto,"...") != -1:
        return str.count(texto,"...")    
    
    elif str.find(texto,"!") != -1:
        return str.count(texto,"!")
    
    elif str.find(texto,"?") != -1:
        return str.count(texto,"?")

    elif str.find(texto,".") != -1:
        return str.count(texto,".")    
    
    else:
        return 0