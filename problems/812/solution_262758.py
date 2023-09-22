def retira_pontos(s):
    pontos=['.','-',';',',',':']
    s_semponto=[s.replace(i,' ') for i in pontos]
    return s_semponto