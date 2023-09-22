def conta_frases(frase):
    
    ls1=str.partition(frase,".") and str.split(frase,"!") and str.split("?") and str.split("...")
    
    return len(ls1)