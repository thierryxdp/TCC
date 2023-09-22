def retira_pontuacao(frase):
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

def inverte(frase):
    """funcao que retorna a frase de entrada invertida, sem pontuação e com letras minusculas;
    string -> string"""
    frase_invertida_em_lista=str.split(retira_pontuacao(frase),' ')[-1::-1]
    return str.strip(str.lower(str.join(' ',frase_invertida_em_lista)))