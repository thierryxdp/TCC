def retira_pontuacao(frase):
    """recebe uma string com uma frase e retorna uma string com a mesma frase
    com seus caracteres de pontuação substituidos por espaço"""

    frase1 = frase.replace("-", " ")
    frase2 = frase1.replace(",", "")
    frase3 = frase2.replace(":", " ")
    frase4 = frase3.replace(";", " ")
    frase5 = frase4.replace(".", "")
    frase6 = frase5.replace("!", " ")
    frase7 = frase6.replace("?", " ")
    
    return frase7

def inverte(frase):
    """Recebe uma frase e retorna as mesmas palavras em ordem inversa
    str->str """
    texto = retira_pontuacao(frase)
    frase_espaco = texto.replace(" ", " / ") #troca espaço por /
    frase1 = str.lower(frase_espaco) #coloca em minúsculo
        
    frase2 = frase1.split() #separa palavras
    list.reverse(frase2) #reverte a lista

    frase_final = "".join(frase2) #une a lista
    frase_unida = frase_final.replace("/", " ") #troca / por espaço
    
    
    return frase_unida