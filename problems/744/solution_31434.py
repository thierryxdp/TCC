# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    string_tamanho = len(s)
    string_meio = string_tamanho // 2
    s_corrigido = s[:0] + '#' + s[0:string_meio] + '#' + s[string_meio:string_tamanho] + '#'
    return s_corrigido