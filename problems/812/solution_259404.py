def retira_pontuacao(frase: str) -> str:
    lamb = lambda x: " " if x in ".,-:;" else x
    changed = map(lamb, frase)
    return "".join(changed)