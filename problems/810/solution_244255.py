def retira_pontuacao(frase):
    """Dada uma frase, retorna ela sem pontuação
    str -> str"""
    sem_pontos = str.replace(str.replace(str.replace(frase,","," "),"."," "),"..."," ")
    sem_pontos2= str.replace(str.replace(str.replace(sem_pontos,"!"," "),"?"," "),";"," ")
    return str.replace(str.replace(sem_pontos2, ":", " "), "-"," ")

def inverte(frase):
    """Dada uma frase, inverte ela sem letras maiúsculas e sem pontuação
    str -> str"""
    lista = str.split(retira_pontuacao(str.lower(frase)))
    return str.join(" ",lista[::-1])