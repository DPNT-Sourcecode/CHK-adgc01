
from checkout_solution import checkout

testData = [
    { "basket" : "",      "expectedSum" : 0 },
    { "basket" : "A",     "expectedSum" : 50 },
    { "basket" : "B",     "expectedSum" : 30 },
    { "basket" : "C",     "expectedSum" : 20 },
    { "basket" : "D",     "expectedSum" : 15 },
    { "basket" : "E",     "expectedSum" : 40 },
    { "basket" : "ABCDE", "expectedSum" : 155 },
    { "basket" : "AAA",   "expectedSum" : 130 },
    { "basket" : "AAAA",  "expectedSum" : 180 },
]

def test_checkout():
    for test in testData:
        basket, expectedSum = test["basket"], test["expectedSum"]
        receivedSum = checkout(basket)
        print(f"Basket => {basket}. Expected '{expectedSum}', got '{receivedSum}'")
        assert receivedSum == expectedSum
    
    print("Passed")
    pass


test_checkout()

