def retira_pontuacao(texto):
    '''Escreva um texto entre "". A funcao retorna o mesmo texto com as
    pontuacoes transformadas em barra de espaco (" ").
    #parametros | in: str (texto de entrada) -> out: str (texto transformado)'''
    #transformando cada pontuacao em ".":
    x1=texto.replace('!','.')
    x2=x1.replace(';','.')
    x3=x2.replace(':','.')
    x4=x3.replace('?','.')
    x5=x4.replace('-','.')
    texto_transformado=x5.replace(',','.')
    #transforma todos os "." em espaco:
    return texto_transformado.replace('.',' ')