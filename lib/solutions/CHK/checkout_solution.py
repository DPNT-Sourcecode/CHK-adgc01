

from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # verify input
    if(not isinstance(skus, str)) :
        return -1
    else :
        print(skus)
        return 2
        # define special offers (not yet)
        # split string into list & count occurrences of each character
        # skus = list(skus)
        # basket = Counter(skus)

        # # return sum
        # basketSum = 0
        # for item, count in basket.items():
        #     basket +=
        
    



