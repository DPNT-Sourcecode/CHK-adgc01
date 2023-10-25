from collections import Counter

# nested dict to track sku prices & offers
prices = {
    'A' : {
        'price' : 50,
        'offers' : {
            '5A' : 200,
            '3A' : 130,
            
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
        basket, basketSum = Counter(list(skus)), 0

        # calculate basket sum
        for item, itemCount in basket.items():

            # invalid skus
            if item not in prices:
                return -1
            else :

                # retrieve sku info
                price = prices[item]['price']
                offers = prices[item]['offers']

                # calculate cost of each sku
                for i in range(itemCount):
                    offerApplied = False

                    # offer exist, apply higher offers first
                    for offer, discount in sorted(offers.items()):
                        
                        # retrieve offer quantity e.g. 3A
                        minOfferQuantity = int(offer[0])

                        # apply offers until item count < minimum offer quantities
                        if itemCount >= minOfferQuantity:

                            # apply simple offers
                            if isinstance(discount, int):
                                basketSum += discount
                            
                            # apply bogo discount
                            else:
                                # TODO handle discount for 2E
                                print('TODO Bogo offer')
                            
                        # offer applied, reduce total item count by offer minimum amount (e.g 4A-3A)
                        itemCount -= minOfferQuantity

                        # update offer applied flag & exit
                        offerApplied = True
                        break

                    # doesn't meet offer minimum quantity
                    if not offerApplied : basketSum += price

        return basketSum

print(checkout("B"))




