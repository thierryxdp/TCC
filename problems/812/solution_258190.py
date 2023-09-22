def retira_pontuacao (frase):
    """função que recebe uma frase normal e que retorna uma nova frase sem
    todos os pontos: vírgula, travessão, dois pontos, ponto e vírgula e
    ponto final) e substituir todos eles por um espação;
    string->string"""
    return str.replace(str.replace(str.replace(str.replace(str.replace(frase,'.',' '),';',' '),':',' '),'-',' '),',',' ')