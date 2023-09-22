def conta_frases(frase):
    '''funçao que retorna o número de ocorrência das pontos presentes na frase de entrada''' 
    '''Str->int'''
    a=str.count(frase,"...")
    b=str.count(frase,"!")
    c=str.count(frase,"?")
    d=str.count(frase,".")
    if a!=0:
        return a+b+c+d-3*a
    else:
        return a+b+c+d