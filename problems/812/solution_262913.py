def retira_pontuacao(s):
    a = [".","_", "-", ",", ";", ":","/","?","!"]
    for n in range(len(a)):
        x = a[n]
        s = str.replace(s, x, " ")
    return s