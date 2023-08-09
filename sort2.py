import time

def f(n):
            sortingList : list = []

            with open(n, "r") as bef:
                numbers = str(bef.read())
                sortingList = [int(x) for x in numbers.split(",")]
            bef.close()

            global start_time 
            start_time = time.time()

            for _ in range(len(sortingList)-1):
                for i in range(len(sortingList)-1):
                    if sortingList[i] > sortingList[i+1]:
                        sortingList[i+1],sortingList[i]=sortingList[i],sortingList[i+1]
            
            print("Time to sort :" ,str(time.time() - start_time),"seconds.")

            with open("sorted.txt", "x") as aft:
                for i in range(len(sortingList)):
                    aft.write(str(sortingList[i]))
                    aft.write(",")
            aft.close()

def main():
    try:
        f(str(input("Enter txt file location >>")))
        main()
    except:
        print("Error!")
        main()
main()
