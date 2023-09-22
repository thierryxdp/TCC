def retira_pontuacao(frase):
    """Função que retira as pontuações, '/' , ',' , ':' , '.' ,
    ';' , '!' e retorna índice em branco; str -> str"""

    sem_pontuacao = str.strip( str.strip( str.strip( str.strip(str.strip(str.strip(frase, ','), '.'), '/'), ':'), ';'), '!')
    return sem_pontuacao