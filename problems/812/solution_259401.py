def retira_pontuacao(frase: str) -> str:
    lamb = lambda x: x if x.isalnum() else ' '
    changed = map(lamb, frase)
    return "".join(changed))