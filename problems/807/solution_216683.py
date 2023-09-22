def conta_frases(text):
    """Conta o numero de frases existentes entro do texto fornecido;
    str -> int"""
    
    pontoF = len(str.split(text, '.'))-1
    pontoE = len(str.split(text, '!'))-1
    pontoI = len(str.split(text, '?'))-1
   	pontoR = str.replace(text, '...', '.')
    pontRT = len(str.split(pontoR, '.'))-1
    
    soma= pontoF + pontoE + pontoI + pontRT
    
    return soma