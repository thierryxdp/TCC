def retira_pontuacao(texto):
    """função que retorna o texto de entrada com caracteres que apresentam pontuação susbtituidos por espaços
    Entrada: str
    Saída: str"""
    texto=str.replace(texto,',',' ')
    texto=str.replace(texto,'.',' ')
    texto=str.replace(texto,'-',' ')
    texto=str.replace(texto,':',' ')
    texto=str.replace(texto,';',' ')
    texto=str.replace(texto,'?',' ')
    texto=str.replace(texto,'!',' ')
    texto=str.replace(texto,'...',' ')
    return texto