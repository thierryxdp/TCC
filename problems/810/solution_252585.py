def retira_pontuacao(frase):
    sem_vir = str.replace(frase, ",","")
    sem_dot = str.replace(sem_vir, ".","")
    sem_trv = str.replace(sem_dot, "-"," ")
    sem_exc = str.replace(sem_trv, "!","")
    sem_int = str.replace(sem_exc, "?","")
    frase_sem_pontuacao = sem_int
    return sem_int

def inverte(frase):
    """Dada uma frase, retorna outra frase com as mesmas palavras, porém na
ordem inversa. Sem letras maiúsculas e sem pontuação.
Assinatura: list -> list
Casos de teste:
inverte("Oi, tudo bem?") == 'bem tudo oi'
inverte("Parabéns! Você tirou 10!") == '10 tirou você parabéns'
"""
    frase_semp = retira_pontuacao(frase)
    frase_final = str.lower(frase_semp)
    frase_cort = str.split(frase_final, " ")
    list.reverse(frase_cort)
    frase_invertida = str.join(" ", frase_cort)
    return frase_invertida