
class räknare: #huvud klas för själva räknaren
    def __init__(self):
        pass

        #funktioner för att genomföra dom aritmatioska operationerna

    def adition(self, a , b):
        return a+b
    
    def subtraktion(self, a , b):
        return a-b
    
    def multi_p(self, a , b):
        return a*b

    def division(self, a , b):
        if b==0: # if satsen här säger till så man inte får en valeuerror
            return "can not divide by 0"
        else:
            return a/b

mini_räknare = räknare()#skapar ett objekt från klassen 

resultat= mini_räknare.adition (4,2)
print(resultat)
resultat= mini_räknare.subtraktion (10,5)
print(resultat)
resultat= mini_räknare.multi_p (100,13)
print(resultat)
resultat= mini_räknare.division (12,2)
print(resultat)