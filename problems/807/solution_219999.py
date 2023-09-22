#Criando função conta_frases
def conta_frases (texto : str) -> int:
    '''Recebe um texto e retorna o número de frases nela'''
    
    #Cortando o texto em frases
    if (texto.find('!') != -1):
   		textoA = texto.replace('!', '.')
    if (texto.find('?') != -1):
        textoA = texto.replace('?', '.')
    if (texto.find('...') != -1):
        textoA = texto.replace('...', '.')
        
    return textoA.count('.')