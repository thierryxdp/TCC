def retira_pontuacao (frase):
    '''substitui todos os caracteres de pontuacao por espaço'''
    '''str -> str'''
    frase = frase.replace ("."," ")
    frase = frase.replace (","," ")
    frase = frase.replace ("?"," ")
    frase = frase.replace ("!"," ")
    frase = frase.replace ("-"," ")
    frase = frase.replace (":"," ")
    frase = frase.replace (";"," ")
    return frase

def inverte (frase): 
    '''dada uma frase retorna outra frase com as palavras na ordem inversa, sem letras maiusculas e pontuacao''' '''str -> str''' 
    '''str -> str'''
    f_sem_pontos = retira_pontuacao(frase)
    texto = str.lower(f_sem_pontos)
    resposta = texto[::-1]
    
    return resposta