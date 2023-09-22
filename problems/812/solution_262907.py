def retira_pontuacao(s):
    a = (".","_", "-", ",", ";", ":","/","?","!")
    for n in range(len(a)):
        s = list(s).remove(a[n])
    return join(s)