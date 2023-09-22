def retira_pontuacao(frase):
    
    nova_frase1 = frase.split('-')
    nova_frase2 = frase.split(',')
    nova_frase3 = frase.split(':')
    nova_frase4 = frase.split(';')
    nova_frase5 = frase.split('.')
    nova_frase6 = frase.split('?')
    nova_frase7 = frase.split('!')
    
    return (nova_frase1 + " " + nova_frase2 + " " + nova_frase3 + " " + nova_frase4 + " " + nova_frase5 + " " + nova_frase6 + " " + nova_frase7)