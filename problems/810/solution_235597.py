def retira_pontuacao(frase):
    """funcao que retorna a frase dada substituindo todos os caracteres de pontuacao por espaco
    
       str->str"""
    
    frase= str.replace(frase, "-", " ") 
    frase= str.replace(frase, ".", "")
    frase= str.replace(frase, ":", "")
    frase= str.replace(frase, ",", "")
    frase= str.replace(frase, ";", "")
    frase= str.replace(frase, "!", "")
    frase= str.replace(frase, "?", "")
    
    return frase


def separa_frase(frase):
    """separa as palavras da frase e retorna uma lista com elas
    
    str-> lista
   """
    
    frase_sem_pont= retira_pontuacao(frase)
    
    return str.split(frase_sem_pont," ")


def inverte(frase):
    """inverte a strig fornecida, apresentando-a de tras pra frente
    
         str->str
    """
    
    lista1= separa_frase(frase)
    
    lista_tras_p_frente= lista1[::-1]
    
    string_final= str.join(" ",lista_tras_p_frente)

    return str.lower(string_final)