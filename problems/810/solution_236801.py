# Retira os sinais de pontuaçao de 'frase' e substitui por espaços
# frase: string
def retira_pontuacao(frase):
    """Funçao que retira todos os sinais de pontuacao da string 'frase' e substitui-os por espaço"""
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'...',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'.',' ')
    return frase

# Inverte as palavras de 'frase'
# frase: string
def inverte(frase):
    """Inverte as ordem das palavras contidas na string 'frase', sem letras maiusculas e cuja pontuacao foi retirada na funcao anterior"""
    s = str.split(retira_pontuacao(frase))
    f = s[::-1]
    return str.lower(str.join(' ',f))