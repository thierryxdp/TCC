def retira_pontuacao(frase):
    """Função que retira as pontuações, '/' , ',' , ':' , '.' ,
    ';' e índice em branco; str -> str"""

    sem_pontuacao = str.strip(frase, str.strip(frase, str.strip(frase, str.strip(str.strip(frase, ','), '.'), '/'), ':'), ';')
    return sem_pontuacao