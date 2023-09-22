#Criando função conta_frases
def conta_frases (texto : str) -> int:
    '''Recebe um texto e retorna o número de frases nela'''
    textoA = texto;
    #Substituindo caracteres por caracter comum '.'
    
    textoA = textoA.replace('!','.')
    textoA = textoA.replace('?','.')
    textoA = textoA.replace('...','.')
        
    return textoA.count('.')