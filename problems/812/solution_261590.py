def retira_pontuacao(texto):
    '''funcao que recebida uma frase como entrada retorna a mesma frase com as pontuacoes substituidas por espacos
       str->str'''
    stringvazia=''
    return str.strip(texto,'-.?!:;, ')