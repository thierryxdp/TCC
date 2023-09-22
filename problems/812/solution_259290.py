def retira_pontuacao(x):
    'retira pontuação e coloca espaços'
    pontuacoes= ['--','...','.',',',';',':','!','?']
    return map(str.x.replace,pontuacoes,[' ']*len(pontuacoes))