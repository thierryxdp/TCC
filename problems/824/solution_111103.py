def uppCons(frase):
    '''Função que retorna a frase com todas as suas consoantes em
    maiúsculas.
    frase=str->str'''
    y=0
    vogais=['a','ã','á','à','e','é','ê','i','í','o','ô','õ','ó','u','ú','A','Â','Ã','Á','À','E','É','Ê','I','Í','O','Ó','Ô','Õ','U','Ú']
    while y<len(frase):
        if frase[y] not in vogais:
            frase=str.replace(frase,frase[y],str.upper(frase[x]))
        y=y+1
    return frase