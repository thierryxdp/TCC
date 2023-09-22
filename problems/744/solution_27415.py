# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Insere o caractere # no início, no meio e no fim de uma string
    str -> str
    	Parameters:
        s: String inicial
        
        Returns:
        String inicial com o caractere # no início, meio e final dela
     """
    inicio = s[ :(len(s)//2)]
    final = s[(len(s)//2): ]
    return "#" + inicio + "#" + final + "#"