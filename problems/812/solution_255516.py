def retira_pontuacao(frase): #Recebe uma frase
    pontos = ['-', '!', '?', ',', ';',':','.'] #Pontuação
    frasefinal = [] 
    for letra in frase: #Para cada letra na string recebida ele executa um loop
        if not letra in pontos: #O loop checa se o caractere é uma pontuação ou não
            frasefinal.append(letra) #Caso for, é adicionado em uma lista
        else:
            frasefinal.append(' ') #Caso não, vira um ' '
    return ''.join(frasefinal) #Junta tudo e retorna