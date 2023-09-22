def lingua_p(palavra):
    for vogal in "áaeéiouú":
        nova_palavra= str.replace(palavra,vogal,vogal+'p'+vogal)
    return nova_palavra