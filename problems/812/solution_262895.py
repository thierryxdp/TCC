def retira_pontuacao(s):
    a = (".","_". "-", ",", ";", ":","/","?","!")
    for n in range len(a):
        s = list.pop(s, n)
    return join(s)