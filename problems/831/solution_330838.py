def lingua_p(palavra):
    '''
    funcao que recebe uma palavra e a traduz para a lingua do p
    str->str
    '''
    palavra.lower()
   
	if 'a'  in palavra:
       palavraNova = palavra.replace('a','apa')
    elif 'e' in palavra:
       palavraNova = palavra.replace('e','epe')
    elif 'i' in palavra:
       palavraNova = palavra.replace('i','ipi')
    elif 'o' in palavra:
       palavraNova = palavra.replace('o','opo')
    elif 'u' in palavra:
       palavraNova = palavra.replace('a','upu')

    return palavraNova