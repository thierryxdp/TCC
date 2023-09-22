def retira_pontuacao(a):
    
    dataClean = '' .join(data).lower()
    dataCleann = re.sub('["-,.:@#?!&$]', ' ', dataClean)
    return (dataClean)

'''
dataClean = ''.join(data).lower()
dataClean = re.sub(r'["-,.:@#?!&$]', ' ', dataClean)
print(dataClean)
'''