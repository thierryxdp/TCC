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