def dataClean
dataClean = ''.join(data).lower()
dataClean = re.sub(r'["-,.:@#?!&$]', ' ', dataClean)
return (dataClean)