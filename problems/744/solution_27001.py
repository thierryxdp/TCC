# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """ Recebe uma string e retorne essa string com # no início, meio e fim.
        
        Parameters:
            s = string inserida a ser alterada (deve ser digitada entre aspas)
        
        Testes:
            hashtag("abcd") = #ab#cd#
            hashtag("abcde") = ab#cde#

        Returns:
            Retorna a string string inserida com # no início, meio e fim.
            str -> str.
    """
    tamanho = len(s)
    metade = tamanho // 2
    primeira_parte = s[:metade]
    segunda_parte = s[metade:]
    
    return "#"+primeira_parte+"#"+segunda_parte+"#"