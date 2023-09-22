def uppCons(frase):
    '''Função que retorna a frase com todas as suas consoantes em
    maiúsculas.
    frase=str->str'''
    x=0
    vogal=['a','ã','á','à','e','é','ê','i','í','o','ô','õ','ó','u','ú','A','Â','Ã','Á','À','E','É','Ê','I','Í','O','Ó','Ô','Õ','U','Ú']
    while x<len(frase):
        if frase[x] not in vogal:
            frase=str.replace(frase,frase[x],str.upper(frase[x]))
        x=x+1
    return frase