import numpy as np

def shuffles(k, n, loops):
    avg_list = []
    for i in range(loops):
        idx_list = np.arange(1, n+1, dtype=int)

        np.random.shuffle(idx_list)

        avg_list.append(np.average(idx_list[0:20]))
        avg_list.append(np.average(idx_list[20:40]))
        avg_list.append(np.average(idx_list[40:60]))
        avg_list.append(np.average(idx_list[60:80]))
        avg_list.append(np.average(idx_list[80:]))
    
    with open("shuffle.txt", 'w') as output:
        for avg in avg_list:
            output.write(str(avg) + '\n')
    return

def combinations(k, n, loops):
    avg_list = []
    for i in range(loops):
        idx_list = np.arange(1, n+1, dtype=int)
        for j in range(k):
            rng_list = np.random.randint(0, len(idx_list), size=int(np.round(n/k)))
            avg_list.append(np.average(idx_list[rng_list]))
            
            mask = np.full(len(idx_list), True)
            mask[rng_list] = False

            idx_list = np.array(idx_list)[mask]
    
    with open("choose.txt", 'w') as output:
        for avg in avg_list:
            output.write(str(avg) + '\n')
    return

def main():
    k = 5
    n = 100
    loops = 10
    np.random.seed(50)
    shuffles(k, n, loops)
    combinations(k, n, loops)
    return

if __name__ == "__main__":
    main()