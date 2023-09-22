def conta_frases(frase):
    
    tamanho1=frase.replace('!','.')
    tamanho2=tamanho1.replace('?','.')
    tamanho3=tamanho2.replace('...','.')
    
    return len(tamanho3.split('.'))-1