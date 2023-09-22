def inverte(frase1):
    """Inverte a frase da entrada retirando as pontuações
     str -> str"""
    frase_limpa = retira_pontuacao(frase1)
    fpronta = str.lower(frase_limpa)
    fpartes = str.split(fpronta, " ")
    list.reverse(fpartes)
    resposta = str.join(" ", fpartes)
    return resposta