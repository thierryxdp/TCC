def retira_pontuacao(frase):
    '''Dada uma frase, retorna todos os caracteres de pontuação substituídos por espaços; string -> string'''
    frase = frase.split('...' )
	frase = str(frase).split('.' )
	frase = str(frase).split('?' )
    frase = str(frase).split('!' )
    frase = str(frase).split('-' )
    frase = str(frase).split(' ' )
    frase = str(frase).split(':' )
    frase = str(frase).split(';' )
    return str(frase).join