def retira_pontuacao(s):
    """Função que informado uma frase, substitua as pontuações por espaços
strin -> string
testes:
retira_pontuacao("Victor Marinho. Estuda computação... É professor? Um dia vai se formar... não poderei ir,
entretanto;  minhas comidas favoritas são:") == 'Victor Marinho  Estuda computação    É professor  Um dia vai se formar    não poderei ir
entretanto   minhas comidas favoritas são '
retira_pontuacao("oi. tudo, bem? victor... silveira! marinho: aula de- computacao;") == 'oi  tudo  bem  victor    silveira  marinho  aula de  computacao '
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