def retira_pontuacao(frase: str) -> str:
    return str.join("", [" " if (c in "-,:;.!?") else c for c in frase])