from Matrix import Matrix

m1 = Matrix.createMatrixUsingExcelFiles("matrix1.xlsx","Matrix 1")
m2 = Matrix.createMatrixUsingExcelFiles("matrix2.xlsx","Matrix 2")

mSum = m1.sum(m2)
mSum.report()
mSum.saveMatrixInExcelFile()

