def uppCons(frase):
    """Retorna frase com todas as suas consuantes maiúsculas.
    srt->str"""
    prox=0
    
    while prox<len(frase):
        if frase[prox]  in 'bcdfghjklmnpqrstvwxyzç':
            frase = str.replace(frase,frase[prox],str.upper(frase[prox]))
        prox=prox+1
        
    return frase