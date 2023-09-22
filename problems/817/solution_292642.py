def acima_da_media(**args):
    above_avg = []
    mean_val = sum(args)/len(args)
    for i in range(len(args)):
        if args[i] > above_avg:
            above_avg.append(args[i])
    return above_avg