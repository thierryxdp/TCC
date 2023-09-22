def retira_pontuação(dataClean):
dataClean = ''.join(data).lower()
dataClean = re.sub(r'["-,.:@#?!&$]', ' ', dataClean)
print(dataClean)