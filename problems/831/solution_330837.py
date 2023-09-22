def lingua_p(palavra):
    '''
    funcao que recebe uma palavra e a traduz para a lingua do p
    str->str
    '''
    palavra.lower()
   
	if 'a'  in palavra:
       palavraNova = palavra.replace('a','apa')
    if 'e' in palavra:
       palavraNova = palavra.replace('e','epe')
    if 'i' in palavra:
       palavraNova = palavra.replace('i','ipi')
    if 'o' in palavra:
       palavraNova = palavra.replace('o','opo')
    if 'u' in palavra:
       palavraNova = palavra.replace('a','upu')

    return palavraNova