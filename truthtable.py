from itertools import product

class truthtable:
    def __init__(self, bitLength: int, expression: str):
        """ This class generates a truth table for a given math expression.

        Args:
            bitLength (int): The number of bits used for each variable.
            expression (str): The expression to be evaluated.
        """
        if bitLength < 1:
            raise ValueError("bitLength must be greater than 0")
        if expression == "":
            raise ValueError("expression cannot be empty")
        self.bitLength = bitLength
        self.exp = expression
        self.truthtable = []
        self.header = ""
                
    def __variableNameList(self)->list:
        varList = []
        for c in self.exp:
            if c.isalpha and c.islower():
                raise ValueError('Expression should be written with uppercase variable names.')
            if c.isalpha():
                varList.append(c)                
        if len(varList) > 8:
            raise ValueError("Maximal variable count is 8.")
        return varList
    
    def __to_bitList(self, val: int, output: bool=False, maxLength: int=0)->str:
        if output:
            return ','.join(bin(val if val>=0 else val+(1<<self.bitLength))[2:].zfill(maxLength))
        else:
            return ','.join(bin(val if val>=0 else val+(1<<self.bitLength))[2:].zfill(self.bitLength))
        
    def generateTable(self)->list:
        """ This function generates the truth table.

        Returns:
            list: The truth table.
        """
        varList = self.__variableNameList()
        resultList = []
        table = []
        for items in product(range(2**self.bitLength), repeat=len(varList)):
            row = []
            for val in items:
                row.append(self.__to_bitList(val))
            table.append(','.join(row))
            resultList.append(eval(self.exp, {c:i for c,i in zip(varList, items)}))
        maxLength = int(max(resultList, key=abs))
        maxLength = maxLength.bit_length()
        
        self.header = (','.join(['{}{}'.format(v,i) for v in self.__variableNameList() for i in range(self.bitLength-1,-1,-1)]) 
                 + ',,' + ','.join(['Q{}'.format(i) for i in range(maxLength-1,-1,-1)]))      
        for index, item in enumerate(table):
            item = item + ',,' + self.__to_bitList(resultList[index], output=True, maxLength=maxLength)
            self.truthtable.append(item)
        return self.truthtable
    
    def printTable(self):
        """ This function prints the truth table in csv form.
        """
        if self.truthtable == []:
            self.generateTable()
        print(self.header)
        print(*self.truthtable, sep='\n')
            
        
    def writeTableCSV(self, filename: str):
        """This function writes the truth table to a csv file.

        Args:
            filename (str): The name of the file to be written.
        """
        if self.truthtable == []:
            self.generateTable()
        with open(filename, 'w') as f:
            f.write(self.header + '\n')
            f.write('\n'.join(self.truthtable))