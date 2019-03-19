import pizza
import read
import functions
import output

inputFiles=["a_example.in","b_small.in","c_medium.in","d_big.in"]
outputFiles=["output_a.txt","output_b.txt","output_c.txt","output_d.txt"]

for f in range(4):
    arguments, lines = read.ReadFile(inputFiles[f])

    p = pizza.Pizza(arguments, lines)
    for i in range(p.R):
        for j in range(p.C):
            if (p.grid[i][j] != 'X'):
                x = functions.biggestViableSlice(i, j, p)
                if x is not None:
                    p.addSlice(x)
    output.Print(outputFiles[f],p.slicelist)
