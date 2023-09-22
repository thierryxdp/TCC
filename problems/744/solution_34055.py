def hashtag(s):
    '''Função que retorna uma string com o caractere # inserido
    no ínicio, meio e fim da string fornecida
    str => str'''
    meio = len(s)//2
    string = "#"+ s[:meio] + "#" + s[meio:] +"#"
    return string