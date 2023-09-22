def retira_pontuacao(frase):
    '''
    	Funcao recebe uma string com uma frase 
        e retorna a frase com todos os caracteres 
        de pontuacaoo substituidos por espaço
        str -> str
    '''
    return ((((((((frase.replace('-',' ')).replace(',',' ')).replace(';',' ')).replace(':',' ')).replace('.',' ')).replace('!',' ')).replace('?',' ')).replace('...',' '))