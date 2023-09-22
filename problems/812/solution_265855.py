def retira_pontuacao(a):
    
    dataClean = '' .join(a).lower()
    dataCleann = .sub('["-,.:@#?!&$]', ' ', dataClean)
    return (dataClean)