# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Coloca hasgtags no início, meio e fim da string"""
    return f"#{s[0:1]}#{s[-1:-2:-1]}#"