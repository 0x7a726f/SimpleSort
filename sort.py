import random as rand
import time
import matplotlib.pyplot as plt

def f(n):
            sortingList : list = []
            for i in range(1,n+1):
                sortingList.append(rand.randint(1,100))
            rand.shuffle(sortingList)

            global start_time 
            start_time = time.time()

            for j in range(len(sortingList)-1):
                for i in range(len(sortingList)-1):
                    if sortingList[i] > sortingList[i+1]:
                        sortingList[i+1],sortingList[i]=sortingList[i],sortingList[i+1]
            return( (time.time() - start_time))
            
def g(n):
    xpoints : list = []
    ypoints : list = []
    for i in range(1,int(n/500)+1):
        xpoints.append(i*500)
        ypoints.append(f(i*500))
    plt.plot(xpoints, ypoints)
    plt.show()

def main():
    try:
        g(int(input("Input Number of Elements (Multiples of 500) >>")))
        main()
    except:
        main()
main()
