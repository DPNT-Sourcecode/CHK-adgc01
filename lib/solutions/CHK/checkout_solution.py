

from collections import Counter

# nested dict to track sku prices & offers
prices = {
    'A' : {
        'price' : 50,
        'offer' : {
            'count' : 3,
            'discount_price' : 130,
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
    'E' : {
        'price' : 40,
        'offer' : {
            'count' : 2,
            'discount_price' : 10,
        },
    },
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # invalid input
    if(not isinstance(skus, str)) :
        return -1
    else :
        # split string into list & count occurrences of each character
        skus = list(skus)
        basket = Counter(skus)

        # calculate basket sum
        basketSum = 0
        for item, itemPrice in basket.items():

            # invalid skus
            if item not in prices:
                return -1
            else :

                # check for offers
                if('offer' in prices[item]):

                    # base prices apply
                    if(itemPrice < prices[item]['offer']['count']):
                        basketSum += (itemPrice * prices[item]['price'])

                    # offer prices apply
                    else:

                        # apply offer multiple times
                        if(itemPrice % prices[item]['offer']['count'] == 0 ):
                            basketSum += (itemPrice/prices[item]['offer']['count']) * prices[item]['offer']['discount_price']
                            print(basketSum)
                        
                        # some quantities qualify for offer
                        else:
                            print("some quantities")
                            offerEligible = (itemPrice // prices[item]['offer']['count']) * prices[item]['offer']['discount_price']
                            offerInEligible = (itemPrice % prices[item]['offer']['count']) * prices[item]['price']
                            basketSum += offerEligible + offerInEligible

                # doesn't meet offer minimum
                else :
                    basketSum += (itemPrice * prices[item]['price'])

        return basketSum


print(checkout("AAABEE"))

