# Função que calcula e retorna o número de frases 
# (terminadas com ponto final, de exclamação, interrogação ou reticências) 
# em um texto de entrada
# string -> int
def conta_frases(texto):
    lista_frase=str.split(texto,'.')+str.split(texto,'...')+str.split(texto,'!')
    return len(lista_frase)