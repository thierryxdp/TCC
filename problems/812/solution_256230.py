# Dada a string frase, esta função retorna a mesma frase, porém com todos os
# caracteres de pontuação sendo substituídos por espaços em branco.
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