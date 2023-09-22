def retira_pontuacao(frase):
    """dada uma string frase de entrada retorna a mesma no entanto com espaços no lugar
    dos caracteres de pontuação
    str --> str"""
    nova_Frase=str.replace(frase,'-',' ')
    nova_Frase=str.replace(nova_Frase,',',' ')
    nova_Frase=str.replace(nova_Frase,':',' ')
    nova_Frase=str.replace(nova_Frase,';',' ')
    nova_Frase=str.replace(nova_Frase,'.',' ')
    nova_Frase=str.replace(nova_Frase,'?',' ')
    nova_Frase=str.replace(nova_Frase,'!',' ')
    nova_Frase=str.replace(nova_Frase,'...',' ')
    return nova_Frase

def inverte(Frase):
    """dada uma string frase de entrada retorna uma nova frase com as mesmas
    palavras da primeira, no entanto com a ordem invertida e sem letras maiúsculas
    str --> str"""
    frase_Repontuada=retira_pontuacao(Frase)
    lista_Frase=str.split(frase_Repontuada)
    list.reverse(lista_Frase)
    frase_Invertida=str.join(' ',lista_Frase)
    return str.lower(frase_Invertida)