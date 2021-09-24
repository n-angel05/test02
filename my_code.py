def counterMethod(idx):
    ctr = 0
    for i in idx:
        ctr += int(idx[i]/2)

    return ctr

def main():
    idx = dict()

    for i in ar:
        if i in idx:
            idx[i] += 1
        else: 
            idx[i] = 1

    print (idx)

    v = counterMethod(idx)
    print (v)



if __name__ == "__main__":

    n = 6
    ar = [1, 2, 1, 2, 1, 3, 2]

    main(n, ar)

