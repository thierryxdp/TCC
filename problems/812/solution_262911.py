def retira_pontuacao(s):
    a = [".","_", "-", ",", ";", ":","/","?","!"]
    for n in range(len(a)):
        x = a[n]
        str.replace(s, x, n)
    return s