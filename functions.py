import math
import pizza


def biggestViableSlice(x, y, puzza):
    found=0
    if puzza.remT>puzza.remM:
        bestVal=float('Inf')
    else:
        bestVal=0
    for h in xrange(puzza.H, 2*puzza.L, -1):
        for (n, m) in findRects(h):
            print n, m
            # Check if its within the borders of the grid
            if(x+n-1 < puzza.R and y+m-1 < puzza.C):
                sslice = pizza.Slice(x, x+n-1, y, y+m-1)
                ratio=ViableSlice(puzza.grid, sslice, puzza.L, puzza.H)
                if ratio>0:
                    found=1
                    if puzza.remT>puzza.remM:
                        if bestVal>ratio:
                            bestVal=ratio
                            bestSlice=sslice
                    else:
                        if bestVal<ratio:
                            bestVal=ratio
                            bestSlice=sslice
        if found:
            return bestSlice
    return None


def ViableSlice(grid, slice, L, H):
    # count the number of elements in slice
    count = 0
    nt = 0
    nm = 0

    for i in range(slice.top, slice.bottom+1):

        for j in range(slice.left, slice.right+1):
            if grid[i][j] == 'M':
                nm += 1
            elif grid[i][j] == 'X':
                return False
            else:
                nt += 1

    if (count > H):
        return 0

    if not (nm >= L and nt >= L):
        return 0

    return float(nm)/nt


def findRects(H):
    mylist = []
    for x in range(1, int(math.sqrt(H)) + 1):
        if(H % x == 0):
            y = H/x
            mylist.append((x, y))
            if(x is not y):
                mylist.append((y, x))

    return mylist
