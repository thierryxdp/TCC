def retira_pontuacao (frase):
    """retorna uma frase onde todos os caracteres
    de pontuação são substituídos por espaço."""
    simbolos = '.!?:;-' 
        return str.replace(frase,simbolos,' ')