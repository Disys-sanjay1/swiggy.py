class user_input:
    def __init__(self):
        self.loc = input("Enter loc : ")

    def h_dis(self,loc):
        if self.loc == "madipakkam":
            self.hot_rate = [{"hotel":"RR biriyani", "rate":"5-star"},
                        {"hotel":"Sangeetha bhavan", "rate":"3.8-star"},
                        {"hotel":"Ambur biriyani", "rate":"4.8-star"},
                        {"hotel":"al-arabian", "rate":"3-star"}]
        elif self.loc == "mylapore":
            self.hot_rate = [{"hotel":"RR biriyani", "rate":"5-star"},
                        {"hotel":"Sangeetha bhavan", "rate":"3.8-star"},
                        {"hotel":"Ambur biriyani", "rate":"4.8-star"},
                        {"hotel":"al-alabian", "rate":"3-star"}]
        elif self.area == "velacherry":
            self.hot_rate = [{"hotel":"RR biriyani", "rate":"5-star"},
                        {"hotel":"Sangeetha bhavan", "rate":"3.8-star"},
                        {"hotel":"Ambur biriyani", "rate":"4.8-star"},
                        {"hotel":"al-arabian", "rate":"3-star"}]
        elif self.area == "saidapet":
            self.hot_rate = [{"hotel":"RR biriyani", "rate":"5-star"},
                        {"hotel":"Sangeetha bhavan", "rate":"3.8-star"},
                        {"hotel":"Ambur biriyani", "rate":"4.8-star"},
                        {"hotel":"al-arabian", "rate":"3-star"}]
        else:
            print("loc out of survey!")
    def disp(self):        
        for i in self.hot_rate:
            f={}
            f=i
            for k,v in f.items():
                print(k,"\t--- \t",v,)

class hot_sel(user_input):
    def __init__(self):
        self.uh = input("Enter hotel: ")
        self.h=["RR biriyani","Sangeetha bhavan","Ambur biriyani","al-arabian"]
        #fself.di()


    def di(self):
        for i in self.h:
            print("\n",i)

    def uh_val(self):
        for i in self.h:
            if (i != self.uh):
                raise ValueError("Invalid hotel")

class dish(hot_sel):
    def __init__(self):
        self.f=["dish1","dish2","dish3","dish4","dish5"]
        self.disp()
        self.user_dis= input("Enter dish: ")

    def dish_val(self):
        for i in self.f:
            if (i != self.user_dis):
                raise ValueError ("dish not available")
            else:
                print("Packing....")
                break

    def disp(self):
        print("\n Available dish")
        print("---------------")
        for i in self.f:
            print(i)
class swiggy:
    def __init__(self,loc,hotel,dish):
        self.p = loc
        self.h = hotel
        self.d = dish

    def beforeorder(self):
        print("order details",self.p,self.h,self.d)

    def display(self):
        print("order confirmed :",self.d," \n @",self.h," in ",self.p)

class user_dis(swiggy):
    def __init__(self):
        self.bill = 1000
        self.sgst = 10
        self.cgst = 15
        self.total = (self.bill+self.sgst+self.cgst)

    def delivery(self):
        self.addr = input("Enter address: ")


    def addvalid(self):
        if isinstance (self.addr,str):
            if isinstance(len(self.addr) <= 30):
                raise ValueError ("enter valid address")
            elif self.addr != None:
                raise ValueError ("invalid address")


    def display(self):
        print("Delivary address : ",self.addr)
        print("Total bill Rs.",self.total)
        ob1.display()


ob = user_input()
ob.h_dis(ob.loc)
ob.disp()
h = hot_sel()
d = dish()
d.dish_val()
ob1 = swiggy(ob.loc,h.uh,d.user_dis)
ob1.beforeorder()
ob2 = user_dis()

ob2.delivery()
ob2.addvalid
ob2.display()
