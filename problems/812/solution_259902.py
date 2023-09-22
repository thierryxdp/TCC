def retira_pontuacao(frase):
    "Substitui todos os caracteres de pontuação de uma frase por espaço. str -> str"
    fraseAlterada = frase
    fraseAlterada = fraseAlterada.replace(".", " ")
    fraseAlterada = fraseAlterada.replace(",", " ")
    fraseAlterada = fraseAlterada.replace(";", " ")
    fraseAlterada = fraseAlterada.replace(":", " ")
    fraseAlterada = fraseAlterada.replace("-", " ")
    fraseAlterada = fraseAlterada.replace("!", " ")
    fraseAlterada = fraseAlterada.replace("?", " ")
    fraseAlterada = fraseAlterada.replace("...", " ")
    return fraseAlterada