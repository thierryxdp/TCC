def retira_pontuacao(s):
    s.strip(",-")
    return s.strip("-:;.!?,")+" "