def retira_pontuacao(frase):
    """Dada uma frase retira o que há de travessão, vírgula, dois pontos,
       dois pontos e vírgula, além da pontuação de encerramento de frase.
       str -> str"""
    
    return "".join([char if char in ".!?," else "" for char in frase)