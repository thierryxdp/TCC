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

def inverte(frase):
    """dada uma string frase de entrada retorna uma nova frase com as mesmas
    palavras da primeira, no entanto com a ordem invertida
    str --> str"""
    frase_Repontuada=retira_pontuacao(frase)
    lista_Frase=str.split(frase_Repontuada)
    lista_Invertida=list.reverse(lista_Frase)
    return str.join('',lista_Invertida)