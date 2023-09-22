def conta_frases(string):
    """dada uma string de entrada entre aspas simples, 
    retorna o numero de frases presentes na mesma"""
    s=string.replace('?','.')
    s=s.replace('!','.')
    s=s.replace('...','.')
    return len(s.split('.'))-1