def uppCons(frase):
    '''Funcao que retorna a frase de entrada com todas as sua consoantes em maiusculas'''
    x=0
    vogal=['a','ã','á','à','e','é','ê','i','í','o','ô','õ','ó','u','ú','A','Á','Ã','Â','À','E','É','Ê','I','Í','O','Ó','Ô','Õ','U','Ú']
    while x<len(frase):
        if frase[x] not in vogal:
            frase=str.replace(frase,frase[x],str.upper(frase[x]))
        x=x+1
    return frase