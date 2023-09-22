def retira_pontuacao(s):
    pontos = ['.','-',',',':',';','.']
    s_semponto=[s.replace(i, ' ') for i in pontos]
    return s_semponto