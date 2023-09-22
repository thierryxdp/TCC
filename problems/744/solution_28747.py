# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """
    Função recebe uma string e insere o caracter '#' no inicio, no meio 
    e no final dela. 
    Parâmetro de Entrada: String
    Valor de Saida: String
    """
    string_hashtag=''
    
    meio=len(s)//2
    
    s_comeco = s[:meio]
    s_fim    = s[meio:]
    string_hashtag= string_hashtag + '#' + s_comeco + '#' + s_fim + '#'
    
    return string_hashtag