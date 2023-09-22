def retira_pontuacao(frase):
    """Substitui todos os caracteres de pontuacao por espacos
    	string --> string"""
    nova_frase = str.replace(frase,'.', ' ')
    nova_frase = str.replace(nova_frase,',', ' ')
    nova_frase = str.replace(nova_frase,'-', ' ')
    nova_frase = str.replace(nova_frase,':', ' ')
    nova_frase = str.replace(nova_frase,';', ' ')
    nova_frase = str.replace(nova_frase,'?', ' ')
    nova_frase = str.replace(nova_frase,'!', ' ')
    return nova_frase