def inverte(frase):
    '''Função que dada um frase, retorne uma outra frase que contenha as mesmas
       palavras da frase de entrada na ordem inversa sem letras maíusculas e sem pontuação.
       str ---> str'''
    frase = frase.lower()
    final = str.replace(frase,',','')
    final = str.replace(final,':','')
    final = str.replace(final,';','')
    final = str.replace(final,'.','')
    final = str.replace(final,'-','')
    lista = str.split(final)
    list.reverse(lista)
    return str.join(' ',lista)