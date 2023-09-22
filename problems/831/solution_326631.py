def lingua_p(palavra):
    for vogal in "áaeéiouú":
        palavra= str.replace(palavra,vogal,vogal+'p'+vogal)
    return palavra