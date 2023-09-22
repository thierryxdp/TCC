# Dada a string frase, esta função irá retirar todos os caracteres de pontuação
# e trocá-los por espaços em branco.
# str -> str

def retira_pontuacao(frase):
    frase = frase.replace('-',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    return frase