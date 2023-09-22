def uppCons(frase):
    """
    
    """
    vogais=("a","e","i","o","u","A","E","I","O","U","á","é","í","ó","ú","ã","õ","â","Á","É","Í","Ó","Ú","Ã","Õ","Â")
    i=0
    frasefinal=""
    while i<len(frase):
        if frase[i] not in vogais:
            frasefinal+=str.upper(frase[i])
            i+=1
        frasefinal+=frase[i]
        i+=1
    return frasefinal