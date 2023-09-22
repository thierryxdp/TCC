def lingua_p(palavra):
    palavras = palavra.split('a')
    for i in palavra:
        if i == 'A' or i == 'a' or i == 'E' or i == 'e' or i == 'I' or i == 'i' or i == 'O' or i == 'o' or i == 'U' or i == 'u':
			palavras += 'p'
   	 return palavras