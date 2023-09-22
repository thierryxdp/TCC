def retira_pontuacao(a):
    
    dataClean = '' .join(a).lower()
    dataCleann = re.sub('["-,.:@#?!&$]', ' ', dataClean)
    return (dataClean)