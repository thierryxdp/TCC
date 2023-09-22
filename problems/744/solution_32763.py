# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """funcao recebe uma palavra e insere uma # no inicio,meio e fim.
    funcao conta 0 ate a metade (parte inteira) e concatena com a
    a segunda metade inteira,adicionando os hashtags
    ent->str
    saida->str
    """
    return "#"+s[0:len(s)//2]+"#"+s[len(s)//2:len(s)]+"#"