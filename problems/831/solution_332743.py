def lingua_p(palavra):
    '''função que recebe uma palavra e retorne a mesma
    palavra para a lingua do p. para cada vogal da palavra
    original é inserida uma sequencia de letras p
    mais a vogal original
    str-> str'''
    vogais = ['a','á','à','e','i','o','u','A','Á','À','E','I','O','U']
    nova_palavra = ""
    
    for i in palavra :
        if i in vogais :
            nova_palavra+=i
            nova_palavra+="p"
            nova_palavra+=i
        else :
            nova_palavra+=i
    return (nova_palavra.lower())