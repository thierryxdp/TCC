def upCons(frase):
    '''funcao que retorna a frase com todas as suas conso-
    antes em maisculas'''
    f=0
    vogais=['à','a','á','â','ã','e','é','ê','i','í','o','ó','õ','u','ú,'A','À','Á','Ã','Â','E','É','Ê','I','Í','O','Ó','Õ','Ô','Ú','U']
    while<len(frase):
            if frase[f] not in vogais:
                frase=str.replace(frase,frase[f],str.upper(frase[f]))
            f=f+1
    return frase