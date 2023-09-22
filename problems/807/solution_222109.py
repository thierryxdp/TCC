def conta_frases(frase):
    '''Fazer uma funcao que dada uma string, retorne o numero de frases presentes nela com base na pontuacao;
    str -> int'''
    
    ponto = str.count(frase,'.')
    interrogacao = str.count(frase,'?')
    exclamacao = str.count(frase,'!')
    reticencias = str.count(frase,'...')
    
    final = ponto + interrogacao + exclamacao + reticencias
    
    if reticencias >= 1:
        return final - reticencias * 3
    
    else: 
        return final