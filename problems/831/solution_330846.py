def lingua_p(palavra):
     '''
    funcao que recebe uma palavra e a traduz para a lingua do p
    str->str
    '''
    palavra.lower()
   
    if 'a'  in palavra:
        palavraNova = palavra.replace('a','apa')
    elif 'e' in palavraNova:
        palavraNova = palavraNova.replace('e','epe')
    elif 'i' in palavraNova:
        palavraNova = palavraNova.replace('i','ipi')
    elif 'o' in palavraNova:
        palavraNova = palavraNova.replace('o','opo')
    elif 'u' in palavraNova:
        palavraNova = palavraNova.replace('a','upu')

    return palavraNova