def retira_pontuacao(text):
    return "".join(["" if char in ".!?," else char for char in text])