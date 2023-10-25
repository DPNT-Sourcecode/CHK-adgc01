from collections import Counter

# nested dict to track sku prices & offers
prices = {
    'A' : {
        'price' : 50,
        # 'offer' : {
        #     3 : {
        #         'count' : 3,
        #         'discount_price' : 130
        #     },
        #     5 : {
        #         'count' : 5,
        #         'discount_price' : 200
        #     },
        # },
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
            'discount_price' : 10, # price of E - price of B, offer 2E >>> offer 2B
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
        for item, itemCount in basket.items():

            # invalid skus
            if item not in prices:
                return -1
            else :

                # check for offers
                if 'offer' in prices[item] :

                    # 
                    # base prices apply
                    if itemCount < prices[item]['offer']['count']:
                        basketSum += (itemCount * prices[item]['price'])

                    # offer prices apply
                    else:

                        # apply offer multiple times
                        if itemCount % prices[item]['offer']['count'] == 0 :
                            basketSum += (itemCount/prices[item]['offer']['count']) * prices[item]['offer']['discount_price']
                        
                        # some quantities qualify for offer
                        else:
                            offerEligible = (itemCount // prices[item]['offer']['count']) * prices[item]['offer']['discount_price']
                            offerInEligible = (itemCount % prices[item]['offer']['count']) * prices[item]['price']
                            basketSum += offerEligible + offerInEligible

                # doesn't meet offer minimum
                else :
                    basketSum += (itemCount * prices[item]['price'])

        return basketSum


print(checkout("AAABBEE"))

