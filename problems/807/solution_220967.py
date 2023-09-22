def conta_frases(frase:str)->int:
    numerofrases=frase.count('!')
    numerofrases+=frase.count('?')    
    numerofrases+=frase.count('...')
    numerofrases+=frase.count('.')
    
    numerofrases-=frase.count('...')-2
    return numerofrases