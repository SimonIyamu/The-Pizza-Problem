def Print(outputFile,slicelist):
    output = open(outputFile, "w+")
    numberofslices = len(slicelist)
    output.write(str(numberofslices)+"\n")
    for myslice in slicelist:
        output.write(str(myslice.top)+" "),
        output.write(str(myslice.left) + " "),
        output.write(str(myslice.bottom) + " "),
        output.write(str(myslice.right) + "\n")
    output.close()
