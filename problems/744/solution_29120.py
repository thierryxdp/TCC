# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """adiciona o caractere # no início, no meio e no final da string s;
    string -> string"""
    inicio_da_string=s[:len(s)//2]
    meio_da_string=s[len(s)//2:len(s)//2]
    final_da_string=s[len(s)//2:]
    return "#"+inicio_da_string+"#"+meio_da_string+final_da_string+"#"