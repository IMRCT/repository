from numpy import *

def readfile():
       with open("ch.txt") as file_in:
        lines = []
        for line in file_in:
            lines.append(line)
        return lines

def ParsMatrix(file):
    global m 
    m = Challenge()
    index = 0
    for data in file:
        index += 1
        data = (data.strip()).split(" ")
        if index == 1 :
            m.columns = data[0]
            m.rows = data[1]
            m.snakes = data[2]
        elif index == 2 :
            global Snakes
            Snakes = []
            i = 0
            for i in range(len(data)):
                Snakes.append(Snake())
                r = i + 1
                Snakes[i].lenght = data[i]
        else:
            global mx
            global mat
            mat = Matrix()
            if(index == 3) :
                mx = [[0 for i in range(int(m.columns))] for j in range(int(m.rows))]
            x = 0
            for d in data:
                mx[index-3][x] = d
                if(d == '*'):
                    mat.wormholes += 1
                    mat.wormholescord.append(str(index-3) + ',' + str(x))
                x += 1
            print(mx)
    return
def Searcher():
    for s in Snakes:
        mat.x = 0
        mat.y = 0
def CheckValue(x, y, length):
    

def main():
    ParsMatrix(readfile())
    print(mat.wormholescord)
    return



class Challenge:
    columns = None
    rows = None
    snakes = None
class Snake:
    length = None
class Matrix:
    x = None
    y = None
    wormholes = 0
    wormholescord = []
main()