def conta_frases(text):
    """Conta o numero de frases existentes entro do texto fornecido;
    str -> int"""
    
    v1 = str.replace(text, ".", "...")
   
    pontoE = len(str.split(text, '!'))-1
    pontoI = len(str.split(text, '?'))-1
    pontoR = len(str.split(text, "..."))-1
    
    soma= pontoE + pontoI + pontoR
    
    return soma