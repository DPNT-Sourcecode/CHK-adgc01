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
                                    basketSum += (price * itemCount)

                            # offer applied, reduce total item count by offer minimum amount (e.g 4A-3A)
                            itemCount -= minOfferQuantity
                            offerApplied = True
                            break

                    # no offers applied
                    if not offerApplied :
                        basketSum += price
                        itemCount -= 1

        return basketSum

print(checkout('AAA'))


# def checkout(skus):

#     # invalid input
#     if not isinstance(skus, str):
#         return -1
#     else :

#         basket, basketSum = {}, float('inf')

#         # count occurrences of each sku
#         for sku in skus:
#             if sku in prices:
#                 basket[sku] = basket.get(sku, 0) + 1
#             else:
#                 return -1

#         # generate all offer combinations and select the lowest basket sum to give the customer the best offer
#         offerCombinations = [[]]

#         # calculate basket sum
#         for item, itemCount in basket.items():

#             # retrieve sku info
#             price = prices[item]['price']
#             offers = prices[item]['offers']
#             itemCombinations = []

#             # get offer combinations
#             for offer, discount in sorted(offers.items(), key=sortOffersByHighestQuantity, reverse=True):
#                 # retrieve offer quantity (e.g. 3A)
#                 offerQuantity = int(offer[0])
#                 numCombinations = itemCount // offerQuantity
#                 itemCombinations.extend([offer] * numCombinations)

#             offerCombinations = [ combination + [itemOffer] for combination in offerCombinations for itemOffer in itemCombinations ]

#         # try all offer combinations and pick the one with the lowest amount
#         for offerCombination in offerCombinations:
#             tempBasket = dict(basket)
#             tempBasketSum = 0

#             for itemOffer in offerCombination:
#                 item = itemOffer[-1]
#                 offerQuantity = int(itemOffer[0])
#                 price = prices[item]['price']
#                 offerPrice = prices[item]['offers'][itemOffer]

#                 # apply simple offers
#                 if isinstance(offerPrice, int):
#                     offerCount = tempBasket[item] // offerQuantity
#                     tempBasketSum += offerCount * offerPrice
#                     tempBasket[item] -= offerCount * offerQuantity
                
#                 # apply discount on related item (e.g. 2E => -1B from basket)
#                 else:
#                     # check if basket contains related offer item
#                     relatedItem = offerPrice
#                     relatedItemCount = tempBasket.get(relatedItem, 0)

#                     # apply bogo offer, remove free item from basket
#                     if relatedItemCount > 0:
#                         tempBasketSum += (price * offerQuantity)
#                         tempBasket[relatedItem] -= 1
#                         tempBasket[item] -= offerQuantity
#                     else:
#                         basketSum += (price * itemCount)

#             for item, itemCount in tempBasket.items():
#                 price = prices[item]['price']
#                 tempBasketSum += itemCount * price
        
#             basketSum = min(basketSum, tempBasketSum)
    
#         return basketSum