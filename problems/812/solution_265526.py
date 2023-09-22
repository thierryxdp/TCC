def retira_pontuacao(frase):
    """Dada uma frase e seus caracteres de pontuação,
retorna a mesma com seus caracteres substituídos por espaço.
Assinatura: str -> str
Casos de teste:
retira_pontuacao("Caro Ícaro, seja bem vindo a UFRJ. Saiba que - apesar das dificuldades - será uma experiência única.") == ("Caro Ícaro  seja bem vindo a UFRJ  Saiba que  apesar das dificuldades   será uma experiência única ")
retira_pontuacao("Olá! Como você está? Não esqueça dos seus compromissos.") == ("Olá  Como você está  Não esqueça dos seus compromissos ")
"""
    sem_vir = str.replace(frase, ",", " ")
    sem_dot = str.replace(sem_vir, ".", " ")
    sem_trv = str.replace(sem_dot, "-", " ")
    sem_exc = str.replace(sem_trv, "!", " ")
    sem_int = str.replace(sem_exc, "?", " ")
    frase_sem_pontuacao = sem_int
    return frase_sem_pontuacao