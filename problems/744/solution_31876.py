# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    # Quebrando a string no meio
    esquerda = s[:len(s)//2 + 1]
    direita = s[len(s)//2+1: ]
    
    # Fazer a alteração pedida
    stringFinal = "#" + esquerda + "#" + direita + "#"
    # Ou
    stringFinal = f"#{esquerda}#{direita}#"
    
    return stringFinal