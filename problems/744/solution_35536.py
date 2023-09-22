# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
        '''funcao que dada uma string, retorna o caractere "#" no início, no meio e no final'''
        meio = (len(s)//2)
        return "#" + s[:meio]+"#"+s[meio:]+"#"