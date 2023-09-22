def inverte(frase):
    """A função a partir da frase (string) recebida como
    parâmetro, retornará um outra frase que contará com as
    mesmas palavras da frase de entrada porém em ordem inversa,
    sem letras maiúsculas, e sem a pontuação.
    Entrada: String
    Saída: String"""
    

    frase = frase.replace('.','') and frase.replace(',','') and frase.replace('!','') and frase.replace('?','') and frase.replace(':','') and frase.replace(';','')and frase.replace('-',' ')
    minus = str.lower(frase)
    dividir = str.split(minus)
    invertida = dividir[-1:] + dividir[:-1]
    
    
    return invertida