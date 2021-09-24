def counterMethod(almacen):
    ctr = 0
    for i in almacen:
        ctr += int(almacen[i]/2)

    return ctr

def main():
    almacen = dict()

    for i in ar:
        if i in almacen:
            almacen[i] += 1
        else: 
            almacen[i] = 1

    print (almacen)

    v = counterMethod(almacen)
    print (v)



if __name__ == "__main__":

    n = 6
    ar = [1, 2, 1, 2, 1, 3, 2]

    main(n, ar)

