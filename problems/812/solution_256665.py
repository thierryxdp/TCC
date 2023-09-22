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
    frase = str.relace(frase,'.',' ')
    return frase