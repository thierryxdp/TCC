def retira_pontuacao
dataClean = ''.join(data).lower()
dataClean = re.sub(r'["-,.:@#?!&$]', ' ', dataClean)
return print(dataClean)