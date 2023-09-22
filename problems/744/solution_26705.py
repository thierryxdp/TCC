# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str

def hashtag(s):
    '''Função retorna uma string adicionando o símbolo # no inicio, 
    meio e fim de cada palavra
	string -> string'''
    
	meiolen = (len(s)//2)
	
    return "#"+s[:meiolen]+"#"+s[meiolen:]+"#"