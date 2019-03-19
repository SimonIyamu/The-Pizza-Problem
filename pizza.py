class Pizza:
    def __init__(self, firstline, lines):
        self.R = firstline[0]
        self.C = firstline[1]
        self.L = firstline[2]
        self.H = firstline[3]
        self.grid = lines
        self.slicelist = []

        self.remM=0
        self.remT=0

        for i in range(0, self.R):
            for j in range(0, self.C):
                if self.grid[i][j]=='M':
                    self.remM+=1
                else:
                    self.remT+=1
        print self.remM, self.remT


    def addSlice(self, slice):
        self.slicelist.append(slice)
        for i in range(slice.top, slice.bottom+1):
            for j in range(slice.left, slice.right+1):
                if self.grid[i][j]=='M':
                    self.remM-=1
                else:
                    self.remT-=1
                self.grid[i][j] = 'X'

    def printPizza(self):
        for line in self.grid:
            for item in line:
                print item,
            print ""


class Slice:
    def __init__(self, top, bottom, left, right):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
