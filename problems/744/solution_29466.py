# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    tamanho = len(s)
    meio = int(tamanho / 2)
    if tamanho % 2 == 0:
        return f'#{s[0: meio]}#{s[meio: len(s)]}#'
    if tamanho % 2 == 1:
        return f'#{s[0: meio]}#{s[meio: len(s)]}#'