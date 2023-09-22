def conta_frases (frase):
    '''Função que dada uma frase, retorna o número de frases dentro do parametro
dado com limitação sobre os pontos "ponto final, um ponto de exclamação, um ponto
de interrogação ou três pontos em sequência (reticências)"
    frase - > int'''
    
    sub=frase.replace('...','#')
    sub=sub.replace('!','#')
    sub=sub.replace('.','#')
    sub=sub.replace('?','#')
    sub=sub.replace('…','#')
    


    return str.count(sub,'#')