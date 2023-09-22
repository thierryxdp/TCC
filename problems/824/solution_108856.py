def uppCons(frase):
    """Funcao que coloca todas as consoantes de uma frase em maiusculo;
    Entrada: str
    Saida: str"""
    
    fraseo = []
    indice = 0
         
    while indice < len(frase):
       	if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
            fraseo = fraseo + [str.upper(frase[indice])]
        else:
            fraseo = fraseo + [frase[indice]]
            indice = indice + 1
    return str.join("",fraseo)