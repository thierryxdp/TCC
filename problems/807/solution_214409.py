def conta_frases(frase):
    """calcula o numero de frases que aparecem no texto"""
   
    return len(frase.replace("...","pedro brabo").replace("?","pedro brabo")
.replace("!","pedro brabo").replace(".","pedro brabo"))