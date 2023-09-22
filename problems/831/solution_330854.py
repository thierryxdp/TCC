def lingua_p(palavra1):
     '''
    funcao que recebe uma palavra e a traduz para a lingua do p
    str->str
    '''
   
    if 'a'  in palavra:
        palavraNova = palavra.replace('a','apa')
    if 'e' in palavraNova:
        palavraNova = palavraNova.replace('e','epe')
    if 'i' in palavraNova:
        palavraNova = palavraNova.replace('i','ipi')
    if 'o' in palavraNova:
        palavraNova = palavraNova.replace('o','opo')
    if 'u' in palavraNova:
        palavraNova = palavraNova.replace('a','upu')

    return palavraNova