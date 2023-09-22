# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Coloca hasgtags no início, meio e fim da string"""
    return f"#{s[0:len(s)//2]}#{s[-1:-len(s)//2:-1]}#"