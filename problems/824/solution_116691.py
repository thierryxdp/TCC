def consoantes_maiusculas(frase):
    #Mapa de consoantes minúsculos com 'ç'.
	lowercase = 'bcçdfghjklmnpqrstvwxyz'
    #Mapa de consoantes maiúsculas com 'Ç'.
	uppercase = 'BCÇDFGHJKLMNPQRSTVWXYZ'
    #Cria a tabela de tradução de caracteres.
	tabela = str.maketrans(lowercase, uppercase)
    #Retorna a frase com os caracteres convertidos.
	return frase.translate(tabela)
	
    uppCons = 'e os demais caracteres exatamente como estavam na frase orifinal'
    print(consoantes_maiusculas(uppCons))