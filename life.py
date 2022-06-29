life = []
for i in range(2500):
    life.append("0")

def lifeOutput():
    a=0
    for b in range(50):
        for i in range(49):
            print(life[a], end = ' ')
            a=a+1
        print(life[a])
populationNum = int(input("How many cells will you populate?\n>>"))
for i in range(populationNum):
    print("Position of cell no",i+1)
    x = int(input(">>"))
    life[x-1] = "\u2588"

lifeOutput()

