def retira_pontuacoes(frase):
    """funcao que dada uma frase, retorna a string da frase, mas com seus sinais de pontuação substituídos por espaco;
    string -> string"""
    frase_sem_virgulas=str.join(' ',str.split(frase,','))
    frase_sem_travessao=str.join(' ',str.split(frase_sem_virgulas,'-'))
    frase_sem_ponto_virgula=str.join(' ',str.split(frase_sem_travessao,';'))
    frase_sem_dois_pontos=str.join(' ',str.split(frase_sem_ponto_virgula,':'))
    frase_sem_ponto=str.join(' ',str.split(frase_sem_dois_pontos,'.'))
    frase_sem_pontointerrogacao=str.join(' ',str.split(frase_sem_ponto,'?'))
    frase_sem_pontoexclamacao=str.join(' ',str.split(frase_sem_pontointerrogacao,'!'))
    return frase_sem_pontoexclamacao