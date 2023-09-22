def retira_pontuacao(text):
    """Recebe uma frase e retorna a mesma frase só que sem os caracteres de pontuação; str->str"""
    return "".join([char if char in ".!?," else "" for char in text)