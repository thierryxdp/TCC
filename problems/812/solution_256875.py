def retira_pontuacao(frase):
    """Funcao que retorna a substituicao de caracteres de pontuacao por espaco"""
    retira_travessao=str.replace(frase,'-',' ')
    retira_virgula=str.replace(frase,',',' ')
    retira_ponto=str.replace(frase,'.',' ')
    retira_exclam=str.replace(frase,'!',' ')
    retira_interrog=str.replace(frase,'?',' ')
    total_retira=retira_travessao or retira_virgula or retira_ponto or retira_exclam or retira_interrog
    return total_retira