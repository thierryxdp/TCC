def lingua_p(palavra):
    palavra = palavra.lower()
    vogais = ('a','á','â','ã', 'e','é','ê', 'i','í','î', 'o','ó','ô','õ', 'u','ú','û')

    for i in vogais:
        if(i in palavra):
            palavra = palavra.replace(i, i + 'p' + i)
        
    return palavra