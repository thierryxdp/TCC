"""Na função abaixo, após serem informados a string, o caractere e o número - de tal forma que o número esteja
entre 0 e o comprimento da string -, é devolvida a string dada, mas é colocada na posição representada pelo número
informado o caractere posto na entrada."""

def Substitui(palavra, caractere, número):
    return palavra[0:(número)]+ caractere + palavra[número+1:len(palavra)]