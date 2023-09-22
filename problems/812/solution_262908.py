def retira_pontuacao(s):
    a = (".","_", "-", ",", ";", ":","/","?","!")
    for n in range(len(a)):
        x = a[n]
        s = list(s).remove(x)
    return join(s)