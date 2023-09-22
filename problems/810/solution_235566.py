def filtro(frase): #Recebe uma frase
    pontos = ['-', '!', '?', ',', ';',':','.'] #Pontuação
    frasefinal = [] 
    for letra in frase: #Para cada letra na string recebida ele executa um loop
        if not letra in pontos: #O loop checa se o caractere é uma pontuação ou não
            frasefinal.append(letra) #Caso for, é adicionado em uma lista
        else:
            frasefinal.append(' ') #Caso não, vira um ' '
    return ''.join(frasefinal) #Junta tudo e retorna

def inverte(frase): #Recebe a frase
    frase = frase.lower() #Passa a letra maiuscula para minuscula
    frase = filtro(frase) #Chama a função anterior para tirar as pontuações
    lista = frase.split() #Separa as palavras
    lista.reverse() #Troca a posição das palavras na lsita
    frase_final = ' '.join(lista) #Junta as palavras trocadas com um ' ' as separando
	return frase_final #Retorna a frase final