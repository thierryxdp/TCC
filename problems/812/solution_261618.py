def retira_pontuacao(texto):
    '''funcao que recebida uma frase como entrada retorna a mesma frase com as pontuacoes substituidas por espacos
       str->str'''
    stringvazia=''
    texto= str.replace(texto,',',' ')
    texto= str.replace(texto,'.',' ')
    texto= str.replace(texto,';',' ')
    texto= str.replace(texto,'-',' ')
    texto= str.replace(texto,':',' ')
    texto= str.replace(texto,'?',' ')
    texto= str.replace(texto,'!',' ')
    return texto