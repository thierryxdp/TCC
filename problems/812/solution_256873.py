def retira_pontuacao(frase):
    """Funcao que retorna a substituicao de caracteres de pontuacao por espaco"""
    retira_travessao=str.replace(frase,'-',' ')
    retira_virgula=str.replace(frase,',',' ')
    retira_ponto=str.replace(frase,'.',' ')
    retira_exclam=str.replace(frase,'!',' ')
    retira_interrog=str.replace(frase,'?',' ')
    total_retira=retira_travessao,retira_virgula,retira_ponto,retira_exclam,retira_interrog
    return total_retira