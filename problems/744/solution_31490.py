# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """
    	Função que recebe uma string e insere o caractere '#' no
        início, no meio e no final dela
        string->
    """
    string = "#"+s+"#"
    meio = len(s)//2
    if len(s)%2==0:
        return string[:meio]+"#"+string[meio:]