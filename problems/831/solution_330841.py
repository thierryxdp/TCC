def lingua_p(palavra):
    '''
    funcao que recebe uma palavra e a traduz para a lingua do p
    str->str
    '''
    palavra.lower()
   
	if 'a'  in palavra:
        palavraNova = palavra.replace('a','apa')
    elif 'e' in palavraNova:
        palavraNova = palavra.replace('e','epe')
    elif 'i' in palavraNova:
        palavraNova = palavra.replace('i','ipi')
    elif 'o' in palavraNova:
        palavraNova = palavra.replace('o','opo')
    elif 'u' in palavraNova:
        palavraNova = palavra.replace('a','upu')
    else:
        palavraNova = palavra

    return palavraNova