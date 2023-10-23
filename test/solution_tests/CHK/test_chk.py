from lib.solutions.CHK.checkout_solution import checkout

testData = {
    { 'skus' : 'AAABB', 'answer' : 175 }
}

for test in testData:
    assert test['answer'] == checkout(test['skus'])
