def inverte(frase):
    '''função que dada uma frase no formato de uma string 
    retorna uma outra frase que contenha as mesams palavras 
    porém na ordem inversa e sem letras maiúsculas e pontuação
    str->str'''
    for pontos in '.!?-,:;':
        frase=frase.replace(pontos,' ')
    frase1=str.lower(frase)
    frase2=str.split(frase1)
    frasenova=frase2[::-1]
    frasenova=str.join(' ',frasenova)
    return frasenova