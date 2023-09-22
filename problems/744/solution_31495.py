def hashtag(s):
    """
    	Função que recebe uma string e insere o caractere '#' no
        início, no meio e no final dela
        string->string
    """
    string = "#"+s+"#"
    meio = len(s) // 2 + 1
    return string[:meio]+ "#" +string[meio:]