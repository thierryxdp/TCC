"""Na função abaixo, após serem informados a string, o caractere e o número - de tal forma que o número esteja
entre 0 e o comprimento da string -, é devolvida a string dada, mas é colocada na posição representada pelo número
informado o caractere posto na entrada."""
def substitui(s, x, i):
    return s[0:(i)]+ x + s[(i+1):len(s)]