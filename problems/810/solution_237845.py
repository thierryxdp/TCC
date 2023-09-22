def retira_pontuacao (frase: str) -> str:
    """Recebe uma frase e retorna a versão da entrada sem os caracteres de
    pontuação, como pontos de exclamação, ponto final, de interrogação..."""
    #Recebe frase sem pontos de exclamação
    frase_1 = str.replace(frase, "!", ' ')
    
    #Recebe frase_1 sem pontos de interrogação
    frase_2 = str.replace(frase_1, "?", ' ')
    
    #Recebe frase_2 sem dois pontos
    frase_3 = str.replace(frase_2, ":", ' ')
    
    #Recebe frase_3 sem ponto e vírgula 
    frase_4 = str.replace(frase_3, ";", ' ')
    
    #Recebe frase_4 sem ponto
    frase_5 = str.replace(frase_4, ".", ' ') #
    
    #Recebe frase_5 sem os três espaços originados ao substituir o ponto por ' ' em reticências
    frase_6 = str.replace(frase_5, "   ", ' ') 
    
    #Recebe frase_6 sem vírgulas
    frase_7 = str.replace(frase_6, ",", ' ')
    
    #Recebe frase_7 sem travessão
    frase_8 = str.replace(frase_7, "-", ' ')
    
    #Recebe o resultado final de todas substituições de pontuação por ' '
    frase_sem_pontuacao = frase_8
    
    return frase_sem_pontuacao

def inverte (frase: str) -> str:
    """Recebe uma string e retorna a mesma sem pontuação, sem letras maiúscula
    e em sua ordem inversa."""
    frase_sem_pontuacao = retira_pontuacao(frase)
    frase_sem_maiuscula = str.lower(frase_sem_pontuacao)
    frase_sem_dois_espacos = str.replace(frase_sem_maiuscula, '  ', ' ')
    #Lista auxiliar que guarda todas palavras - ou elementos- separados por ' '
    lista_aux = str.split(frase_sem_maiuscula, ' ')
    
    #Lista auxiliar que recebe lista_aux com ordem invertida
    lista_aux_invertida = lista_aux [(len(lista_aux)-1)::-1]
    
    frase_alterada = str.join(' ', lista_aux_invertida)
    frase_alterada_final = str.strip(frase_alterada)
    return frase_alterada_final