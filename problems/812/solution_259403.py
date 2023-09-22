def retira_pontuacao(frase: str) -> str:
    pontuacao = ".,-:;"
    lamb = lambda x: ' ' if x in pontuacao else x
    changed = map(lamb, frase)
    return "".join(changed)