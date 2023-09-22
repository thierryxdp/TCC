def inverte(frase):
    " " "Dada uma frase retorna uma outra frase que contem as mesmas palavras da frase de entrada em ordem inversa,sem leetras maiusculas e sem pontuação;str, -> str" " "
    frase = str.replace(frase,'...','.')
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,';',' ')
    frase = str.lower(frase)
    frase_l_inv = str.split(frase)[::-1]
    return str.join(' ',frase_l_inv)