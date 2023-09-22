def lingua_p(palavra):
    '''
    funcao que recebe uma palavra e a traduz para a lingua do p
    str->str
    '''
    palavra.lower()
   
	if 'a'  in palavra:
       palavraNova = palavra.replace('a','apa')
    if 'e' in palavraNova:
       palavraNova = palavra.replace('e','epe')
    if 'i' in palavraNova:
       palavraNova = palavra.replace('i','ipi')
    if 'o' in palavraNova:
       palavraNova = palavra.replace('o','opo')
    if 'u' in palavraNova:
       palavraNova = palavra.replace('a','upu')
    else:
        palavraNova = palavra

    return palavraNova