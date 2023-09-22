def retira_pontuação(frase):
dataClean = ''.join(data).lower()
dataClean = re.sub(r'["-,.:@#?!&$]', ' ', dataClean)
print(dataClean)