class product:
    def __init__ (self,name,price,dealprice,rating):
            self.name=name
            self.price=price
            self.dealprice=dealprice
            self.rating=rating
            self.saveprice=price-dealprice
    def get_product_details(self):
          print("name:{}".format(self.name))
          print("price:{}".format(self.price))
          print("dealprice:{}".format(self.dealprice))
          print("rating:{}".format(self.rating))
          print("saveprice:{}".format(self.saveprice))
class electronicitem(product):
      def setwarranty(self,warranty_in_months):
            self.warranty_in_months=warranty_in_months
      def getwarranty(self):
            return self.warranty_in_months
class groceryitems(product):
      def setexpirydate(self,expirydate):
            self.expirydate=expirydate
      def getexpirydate(self):
            return self.expirydate
e_item=electronicitem("TV",40000,25000,4.5)
e_item.setwarranty(24)
e_item.get_product_details()
print(e_item.getwarranty())
g_item=groceryitems("choci",50,20,4.9)
g_item.setexpirydate("26/12/2025")
g_item.get_product_details()
print(g_item.getexpirydate())