import sys
domain = sys.argv[1]

def perm1():
    #double char
    print(domain.split('.')[0])
    for i in range(len(domain.split('.')[0])):
        permlist = list(domain)
        permlist.insert(i, domain[i])
        permdom = ''.join(permlist)
        print("Doubled char: " + permdom)

    #missing char
    for i in range(len(domain.split('.')[0])):
        #for each letter in position, remove it
        permlist = list(domain)
        permlist.remove(domain[i])
        permdom = ''.join(permlist)
        print("Missing char: " + permdom)

    #horizontal

    #vertical

    #??????


    #bitflip


    #public apis & resources?


perm1()
