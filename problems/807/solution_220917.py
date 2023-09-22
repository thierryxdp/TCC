def conta_frases(string):
    """dada uma string de entrada entre aspas simples, retorna o numero de frases
    presentes na mesma"""
    s=string.replace('?','.')
    s1=s.replace('!','.')
    s2=s1.replace('...','.')
    return len(s2.split('.'))