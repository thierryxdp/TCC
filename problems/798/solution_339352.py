def freq_palavras(frases):
    ct = {}
    for _, value in lds_data.items():
        if value['code_client'] in ct:
            ct [value['code_client']] += 1
            else: ct [value['code_client']] = 1