def lingua_p(frase):
    resposta=''
    vogal=('a','e','i','o','u','á','é','í','ó','ú','ã','õ')
    for letra in frase:
        if letra in vogal:
            resposta= resposta + letra + 'p' + letra
        else:
            resposta=resposta + letra
            
    return resposta