from truthtable import truthtable as exTT

asd = exTT(8,"A==B")
asd.printTable()

asd.writeTableCSV("truthtable.csv")