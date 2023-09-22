def retira_pontuacao(frase):
    """Retorna a frase sem pontuacao.str-->str."""
    a=str.replace(frase,"!"," ")
    b= str.replace(a,"!"," ")