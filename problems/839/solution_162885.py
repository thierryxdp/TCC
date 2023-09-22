def carros(pessoas, lugares=5):
    if pessoas == 0:
        return 0
    elif pessoas < lugares or pessoas == lugares and pessoas != 0:
        return 1
    if pessoas % lugares == 0:
        return pessoas//lugares
    else:
        return (pessoas // lugares) + 1