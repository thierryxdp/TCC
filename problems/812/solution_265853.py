def retira_pontuacao(a):
    
    dataClean = '' .join(data).lower()
    dataCleann = re.sub('["-,.:@#?!&$]', ' ', dataClean)
    return (dataClean)