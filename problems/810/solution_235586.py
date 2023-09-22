def retira_pontuacao(frase):
    """funcao que retorna a frase dada substituindo todos os caracteres de pontuacao por espaco
    
       str->str"""
    
    frase= str.replace(frase, "-", "") 
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


def inverte_lista(frase):
    """inverte a lista fornecida, apresentando-a de tras pra frente"""
    
    lista1= separa_frase(frase)
    
    return str.join(" ",lista1[::-1])