

from collections import Counter

# nested dict to track sku prices & offers
prices = {
    'A' : {
        'price' : '50',
        'offer' : {
            'count' : 3,
            'discount_price' : 150,
        },
    },
    'B' : {
        'price' : 30,
        'offer' : {
            'count' : 2,
            'discount_price' : 45,
        },
    },
    'C' : {
        'price' : 20,
    },
    'D' : {
        'price' : 15,
    },
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # verify input
    if(not isinstance(skus, str)) :
        return -1
    else :
        # define special offers (not yet)
        # split string into list & count occurrences of each character
        skus = list(skus)
        basket = Counter(skus)

        # return sum
        basketSum = 0
        for item, count in basket.items():

            # check for offers
            if item in prices:

                # apply offer price
                if('offer' in prices[item]):
                    if(count >= prices[item]['offer']):

                        # apply offer multiple times if needed
                        if(count % prices[item]['offer']['count'] == 0 ):
                            basketSum += (count/prices[item]['offer']['count']) * prices[item]['offer']['discount_price']
                        else :
                            basketSum += 

            basket +=






