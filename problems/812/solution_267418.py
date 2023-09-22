def retira_pontuacao(texto):
    """Função que substituir "-", ",", ".", ";", ":" por " "(espaço); str->str"""
    texto1=str.replace(texto,'-',' ')
    texto2=str.replace(texto1,',',' ')
    texto3=str.replace(texto2,';',' ')
    texto4=str.replace(texto3,'.',' ')
    texto5=str.replace(texto4,':',' ')
    texto6=str.replace(texto5,'!',' ')
    texto7=str.replace(texto6,'?',' ')
    return texto7