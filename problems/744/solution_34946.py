# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(string):
    '''coloca"#"no inicio meio e fim da strig'''
   string1= "#" + string[:len(string) // 2] + "#" + string[len(string) // 2:] + "#"
   return (string1)