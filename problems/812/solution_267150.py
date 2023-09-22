def retira_pontuacao(s):
    s.replace(","," ")
    return s.strip("-:;.!?,")+" "