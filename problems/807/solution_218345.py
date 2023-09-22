def conta_frases(texto):
    texto4 = str.split(texto,".")
    texto4 = str.rsplit(texto,"?")
    
   
    return len(texto4)