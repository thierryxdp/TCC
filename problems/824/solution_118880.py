def uppCons(frase):
'Função que receba como entrada UMA frase e retorne a frase com todas as suas consoantes maiusculas '''  
''.join(caractere.upper() if caractere in 'bcdfghjklmnpqrstvxwyz' else caractere for caractere in frase)