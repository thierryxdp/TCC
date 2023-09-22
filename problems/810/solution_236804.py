#STRING DO EXERCICIO ANTERIOR, SEM DOCUMENTACAO!
#Professor(a), não consego ver o log da questão anterior.
#Para poupar tempo, colocarei somente a funcao para utilizar na questao.
def retira_pontuacao(texto):
    x1=texto.replace('!','.')
    x2=x1.replace(';','.')
    x3=x2.replace(':','.')
    x4=x3.replace('?','.')
    x5=x4.replace('-','.')
    x6=x5.replace(',','.')
    return x6.replace('.','')
#Questao 5
def inverte(texto):
    '''Escreva um texto entre "". A funcao retorna a frase invertida,
    sem pontuacao e com todas as letras minusculas.
    #parametros | in: str (texto de entrada) -> out: str (texto invertido)'''
    #Transforma o texto, ja transformado, em uma lista ao contrario:
    lista_txt=str.split(str.lower(retira_pontuacao(texto)))[::-1]
    return ' '.join(lista_txt)