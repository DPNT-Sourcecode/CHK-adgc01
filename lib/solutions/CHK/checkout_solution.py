from collections import Counter

# nested dict to track sku prices & offers
prices = {
    'A' : {
        'price' : 50,
        'offers' : {
            '3A' : 130,
            '5A' : 200,
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
        'offers' : { '2E' : 'B' }
    },
}

def sortOffersByHighestQuantity(offer):
    return int(offer[0][0])

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    # invalid input
    if not isinstance(skus, str):
        return -1
    else :

        basket, basketSum = {}, 0

        # count occurrences of each sku
        for sku in skus:
            if sku in prices:
                basket[sku] = basket.get(sku, 0) + 1
            else:
                return -1

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
                while itemCount > 0:
                    offerApplied = False

                    # offer exist, apply higher offers first
                    for offer, discount in sorted(offers.items(), key=sortOffersByHighestQuantity, reverse=True):
                        
                        # retrieve offer quantity (e.g. 3A)
                        minOfferQuantity = int(offer[0])

                        # apply offers until item count < minimum offer quantities
                        if itemCount >= minOfferQuantity:

                            # apply simple offers
                            if isinstance(discount, int):
                                basketSum += discount
                            
                            # apply discount on related item (e.g. 2E => -1B from basket)
                            else:

                                # check if basket contains related offer item
                                relatedItem = discount
                                relatedItemCount = basket.get(relatedItem, 0)

                                # apply bogo offer, remove free item from basket
                                if relatedItemCount > 0:
                                    basketSum += (price * minOfferQuantity)
                                    basket[relatedItem] -= 1
                                else:
                                    basketSum += price

                            # offer applied, reduce total item count by offer minimum amount (e.g 4A-3A)
                            itemCount -= minOfferQuantity

                            # update offer applied flag & exit loop
                            offerApplied = True
                            break

                    # no offers applied
                    if not offerApplied :
                        basketSum += price
                        itemCount -= 1

        return basketSum

print(checkout('AAA'))








