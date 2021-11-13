# Trurth table creator for Logic Friday

Create a truth table any given math or Boolean expression, bit or byte wise, up to 8 variables.

    from truthtable import truthtable as exTT
    tt = exTT(8,"A==B")
   First argument is the bitlength of the variables A and B for this example. String is the expression that you want to evaluate.

    tt.writeTableCSV("truthtable.csv")
  
  With writeTableCSV you can write a csv file that Logic Friday can read. 
