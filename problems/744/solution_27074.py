# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s): 
    """ Funcao que retorna uma string, com ela mesma incluida no seu meio.
    Entrada: str
    Saida: str
    
    parameter:
    s = string escolhida
    """
    
    meio = len(s)//2
    inicio = s[:meio]
    fim = s[meio:]
    
    return "#" +inicio + "#" + fim + "#"