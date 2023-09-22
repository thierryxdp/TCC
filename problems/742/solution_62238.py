# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s, x, i):
    if i >=0 and i<(len(s)):
        if (i < 0):  # add it to the beginning
            return x + s
        if (i > len(s)):  # add it to the end
            return s + x
    else:
        return "Você selecionou um index acima do limite da palavra"

    return s[:i] + x + s[i + 1:]