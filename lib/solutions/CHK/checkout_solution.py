from collections import Counter

# nested dict to track sku prices & offers
prices = {
    'A' : {
        'price' : 50,
        'offers' : {
            '3A' : 130,
            '5A' : 200
        },
    },
    'B' : {
        'price' : 30,
        'offers' : { '2B' : 45 },
    },
    'C' : {
        'price' : 20,
        'offers' : {},
    },
    'D' : {
        'price' : 15,
        'offers' : {},
    },
    'E' : {
        'price' : 40,
        'offers' : { '2E' : 10 } # 2E => -1B
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
        basketSum = 0

        # calculate basket sum
        for item, itemCount in basket.items():

            # invalid skus
            if item not in prices:
                return -1
            else :

                # retrieve sku info
                price = prices[item]['prices']
                offers = prices[item]['offers']

                # calculate 
                for i in range(itemCount):
                    offerApplied = False

                    # check for offers
                    if 'offer' in prices[item] :

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






