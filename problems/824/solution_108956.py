def uppCons(frase):
    """..."""
    contador = 0
    frase_copia = frase[:]
    
    while contador < len(frase):
        if frase[contador] in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']:
            nova_frase = frase[:contador]+str.upper(frase[contador])+frase_copia[contador+1:]
            
        contador=contador+1
        
    return nova_frase