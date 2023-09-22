def retira_pontuacao(s):
    """Recebe frase em formato de string e retorna a mesma frase mas, 
    agora, sem pontuações (travessão, vírgula, dois pontos, ponto e 
    vírgula e ponto)
	assinatura: string --> string
	testes:
    retira_pontuacao('Eu estudo na UFRJ! Curso Bacharelado em Química...') == 'Eu estudo na UFRJ  Curso Bacharelado em Química   '
    retira_pontuacao('Me chamo Estela. Amo química! Moro em São paulo... Estudo no Rio!') == 'Me chamo Estela  Amo química  Moro em São paulo    Estudo no Rio '
    """
    str.replace(s,".", ' ')
    s2 = str.replace(s,".", ' ')
    str.replace(s2,"!", ' ')
    s3 = str.replace(s2,"!", ' ')
    str.replace(s3,"?",' ')
    s4 = str.replace(s3,"?", ' ')
    str.replace(s4,"-", ' ')
    s5 = str.replace(s4,"-", ' ')
    str.replace(s5,",", ' ')
    s6 = str.replace(s5,",", ' ')
    str.replace(s6,";",' ')
    s7 = str.replace(s6,";", ' ')
    str.replace(s7,"...", ' ')
    s8 = str.replace(s7,"...", ' ')
    str.replace(s8,":", ' ')
    s9 = str.replace(s8,":", ' ')
    return s9