

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

        # calculate basket sum
        basketSum = 0
        for item, count in basket.items():

            # invalid skus
            if item not in prices:
                return -1
            else :

                # check for offers
                if('offer' in prices[item]):

                    # check if count of items meets the minimum offer count
                    if(count >= prices[item]['offer']['count']):

                        # apply offer multiple times
                        if(count % prices[item]['offer']['count'] == 0 ):
                            basketSum += (count/prices[item]['offer']['count']) * prices[item]['offer']['discount_price']
                        else:
                            offerEligible = (count // prices[item]['offer']['count']) * prices[item]['offer']['discount_price']
                            offerInEligible = (count % prices[item]['offer']['count']) * prices[item]['price']
                            basketSum += offerEligible + offerInEligible

                # doesn't meet offer minimum
                else :
                    basketSum += count * prices[item]['price']

        return basketSum


print(checkout("AAABB"))








