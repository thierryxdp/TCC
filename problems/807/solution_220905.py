def conta_frases(string):
    """dada uma string de entrada entre aspas simples, retorna o numero de frases
    presentes na mesma"""
    return len(string.split('.','?','!','...'))