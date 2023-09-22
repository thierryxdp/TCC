def lingua_p(palavra):
    '''
    funcao que recebe uma palavra e a traduz para a lingua do p
    str->str
    '''
    palavra.lower()
   
	if 'a'  in palavra:
        palavraNova = palavra.replace('a','apa')
    elif 'e' in palavra:
        palavraNova = palavraNova.replace('e','epe')
    elif 'i' in palavra:
        palavraNova = palavraNova.replace('i','ipi')
    elif 'o' in palavra:
        palavraNova = palavraNova.replace('o','opo')
    elif 'u' in palavra:
        palavraNova = palavraNova.replace('a','upu')
    else:
        palavraNova = palavra

    return palavraNova