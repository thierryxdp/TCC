filtra_pares(t):
    res_list = []
    for sub in test_list:
        res = True
        for ele in sub:
            if ele % 2 != 0:
                res = False
                break
                if res:
                    res_list.append(sub)
                    return str(res_list)