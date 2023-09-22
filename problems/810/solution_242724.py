def retira_pontuacao(frase):
    frase1 = str.replace(frase,"-"," ")
    frase2 = str.replace(frase1,","," ")
    frase3 = str.replace(frase2,":"," ")
    frase4 = str.replace(frase3,";"," ")
    frase5 = str.replace(frase4,"."," ")
    frase6 = str.replace(frase5,"!"," ")
    frase7 = str.replace(frase6,"?"," ")
    return frase7

def inverte(frase):
    """Retorna uma frase que contem as mesmas palavras da original dada como
    entrada, porém na ordem inversa, sem letras maiúsculas e sem pontuação.
str -> str"""
    frase_sem_pontuacao = retira_pontuacao(frase)
    frase_minuscula = str.lower(frase_sem_pontuacao)
    frase_separada = str.split(frase_minuscula)
    list.reverse(frase_separada)
    lista_inversa = frase_separada
    frase_inversa = str.join(" ",lista_inversa)
    return frase_inversa

#Casos de teste:
# inverte("Oi,tudo bem? Eu to bem tambem.") == 'tambem bem to eu bem tudo oi'
# inverte("Que dia LINDO!!!") == 'lindo dia que'