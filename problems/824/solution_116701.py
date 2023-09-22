def uppCons(frase):
    for k in len(frase):
        if k not in ['A','E','I','O','U','a','e','i','o','u','á','é','í','ó','ú','ã','õ','à','è','ì','ò','ù']:
            str.upper(frase,frase[k])
        return frase