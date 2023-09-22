#Recebe uma frase
#1-Retirar os caracteres esperciais 
#2- Transformar em lista retornar o número de frases
def conta_frases(texto:str)->int:
    """A função recebe um texto e retorna o número de frases"""
    import re
    separado=re.split('\. |\! |\? |\.\.\. ', texto)
    return len(separado)