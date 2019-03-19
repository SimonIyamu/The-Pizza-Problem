# Read the input file
def ReadFile(filename):
    FileDesc = open(filename, 'r')
    firstline = FileDesc.readline()
    lines = [list(line.rstrip('\n')) for line in FileDesc]

    firstline = firstline.rstrip('\n').split(' ')

    firstline = list(map(int, firstline))
    return (firstline, lines)
