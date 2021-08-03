from __future__ import print_function
from array import *
# import openpyxl module
import openpyxl
from openpyxl import Workbook

class Matrix:
    
    #numberOfRows = 0
    #numberOfColumns = 0
    #values = [5][5]p'p

    # A constructor gets again matrix's attributes as parameters, however this time it also takes vectorvalues which was
    # given already in the main method is prepared for the matrix's values. 
    # If vectorvalues length is same as our matrix's dimension, it will take it as values.
    # Otherwise, values of the matrix remains as zero, null.

    def __init__(self, title, NumberOfRows, NumberOfColumns, VectorValues = None):
        self.numberOfRows = NumberOfRows
        self.numberOfColumns = NumberOfColumns
        self.title = title

        if(VectorValues == None):
            self.values = [[0 for y in range(self.numberOfColumns)] for x in range(self.numberOfRows)]
        
        elif(len(VectorValues) != NumberOfColumns*NumberOfRows):
            print('the vectorValues array is not suitable for the matrix dimension.')
            
            self.values = [[0 for y in range(self.numberOfColumns)] for x in range(self.numberOfRows)]

        else:
            for i in range(self.numberOfRows):
                for j in range(self.numberOfColumns):
                    self.values[i][j] = VectorValues[i*self.numberOfColumns +j]
    

    #sum up two matrixes which are defined in main
    def sum(self, matrix):

        #if size of two matrixes are equal to each other, summation is possible.
        if(self.numberOfRows == matrix.numberOfRows and self.numberOfColumns == matrix.numberOfColumns):

            resultMatrix = Matrix("Result Matrix",self.numberOfRows,self.numberOfColumns)

            for i in range(self.numberOfRows):
                for j in range(self.numberOfColumns):
                    resultMatrix[i][j] = self.values[i][j] + matrix.values[i][j]
            
            return resultMatrix
        else:
            return None
        
    #report result matrix
    def report(self):

        for i in range(self.numberOfRows):
            print('|', end='')

            for j in range(self.numberOfColumns):
                print(self.values[i][j], end='')
                print(',', end='')
            
            print('|')

    




