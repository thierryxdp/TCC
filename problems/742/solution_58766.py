"""Na função abaixo, após serem informados a string, o caractere e o número - de tal forma que o número esteja
entre 0 e o comprimento da string -, é devolvida a string dada, mas é colocada na posição representada pelo número
informado o caractere posto na entrada."""
def Substitui(s, x, i):
    if i<len(s):
      return s[0:(i - 1)]+ x + s[i:len(s)]