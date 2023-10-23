# import sys
# sys.path.append('C:/Users/mohde/Desktop/accelerate_runner/lib/')

from ..lib.solutions.CHK.checkout_solution import checkout_solution

testData = {
    { 'skus' : 'AAABB', 'answer' : 175 }
}

for test in testData:
    assert test['answer'] == checkout(test['skus'])
