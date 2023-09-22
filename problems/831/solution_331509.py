def lingua_p(palavra):
    '''Função que dada uma palavra retorna ela com a letra p mais a ultima vogal da palavra após essa vogal.
    entrada:str
    saida:str'''
    palavra_p = ""
    for i in range(0,len(palavra)):
        palavra_p = palavra_p + palavra[i]
        if palavra[i] in ["a","e","i","o","u","é","á","ú"]:
            palavra_p = palavra_p + "p" + palavra[i]
    return palavra_p