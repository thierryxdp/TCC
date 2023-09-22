def conta_frases(texto:str)->int:
    #essa função conta o número de frases que tem em um texto
    frases=texto.replace('...','!')
    frases=frases.replace('?','!')
    frases=frases.replace('.','!')
    
    frases=frases.split('!')
    return (len(frases))-1