print("THANK YOU FOR VISITING OUR HOTEL." "\n")
print("your are requested to fill the given form" "\n")
print("PLEASE ENTER YOUR CHOICE" "\n")


class hotelcharge:

    def __init__(self, ttl='', r_rent=0, g_bill=0, f_bill=0, l_bill=0, name='', address='', cindate='', coutdate='',
                 rno=101):

        self.ttl = ttl  # ttl= total bill

        self.f_bill = f_bill  # f_bill = food bill

        self.l_bill = l_bill  # l_bill= laundry bill

        self.g_bill = g_bill  # g_bill= game bill

        self.r_rent = r_rent  # r_rent=room rent

        self.name = name
        self.address = address
        self.cindate = cindate  # check in date
        self.coutdate = coutdate  # check out date
        self.rno = rno  # room number

    def inputdetails(self):
        self.name = input("\nEnter your name:")
        self.address = input("\nEnter your residential address:")
        self.cindate = input("\nEnter your check in date:")
        self.coutdate = input("\nEnter your checkout date:")
        print("Your room no.:", self.rno, "\n")

    def roomrent(self):

        print("We have the following rooms for you:-")

        print("1.  River View Cottage---->Rs 8000 PN\-")

        print("2.  Suite ---->rs 6000 PN\-")

        print("3.  Two Bedded room---->rs 4500 PN\-")

        print("4.  Single Bedded ---->rs 3500 PN\-")

        x = int(input("Enter Your Choice Please->"))

        n = int(input("For How Many Nights Did You Stay:"))  # n=number of nights

        if (x == 1):

            print("you have opted for River View Cottage")

            self.r_rent = 8000 * n

        elif (x == 2):

            print("you have opted For Double bedded suite ")

            self.r_rent = 6000 * n

        elif (x == 3):

            print("you have opted for two bedded room")

            self.r_rent = 4500 * n

        elif (x == 4):
            print("you have opted for Single bedded room")

            self.r_rent = 3500 * n

        else:

            print("please choose a room")

        print("your room rent is =", self.r_rent, "\n")

    def restaurentbill(self):

        print("*****RESTAURANT MENU*****")
        print("1.water----->Rs20")
        print("2.tea----->Rs30")
        print("3.breakfast --->Rs150")
        print("4.lunch---->Rs350")
        print("5.dinner--->Rs500")
        print("6.Breakfast+Lunch+Dinner+Soft Drinks (Buffay)--->Rs2500 /day")

        print("7.Exit")

        while (1):

            c = int(input("Enter your choice:"))

            if (c == 1):
                d = int(input("Enter the quantity:"))  # d=quantity
                self.f_bill = self.f_bill + 20 * d

            elif (c == 2):
                d = int(input("Enter the quantity:"))
                self.f_bill = self.f_bill + 30 * d

            elif (c == 3):
                d = int(input("Enter the quantity:"))
                self.f_bill = self.f_bill + 150 * d

            elif (c == 4):
                d = int(input("Enter the quantity:"))
                self.f_bill = self.f_bill + 350 * d

            elif (c == 5):
                d = int(input("Enter the quantity:"))
                self.f_bill = self.f_bill + 500 * d

            elif (c == 6):
                d = int(input("Enter the quantity:"))
                self.f_bill = self.f_bill + 2500 * d
            elif (c == 7):
                break;
            else:
                print("Invalid option")

        print("Total food Cost=Rs", self.f_bill, "\n")

    def laundrybill(self):
        print("******LAUNDRY MENU*******")

        print("1.Shorts----->Rs10", "2.Trousers----->Rs15", "3.Top/Shirt--->Rs20", "4.Jeans---->Rs50",
              "5.saree--->Rs200",
              "6.Exit")

        while (1):

            e = int(input("Enter your choice:"))

            if (e == 1):
                f = int(input("Enter the quantity:"))  # f=quantity
                self.l_bill = self.l_bill + 10 * f

            elif (e == 2):
                f = int(input("Enter the quantity:"))
                self.l_bill = self.l_bill + 15 * f

            elif (e == 3):
                f = int(input("Enter the quantity:"))
                self.l_bill = self.l_bill + 20 * f

            elif (e == 4):
                f = int(input("Enter the quantity:"))
                self.l_bill = self.l_bill + 50 * f

            elif (e == 5):
                f = int(input("Enter the quantity:"))
                self.l_bill = self.l_bill + 200 * f
            elif (e == 6):
                break;
            else:

                print("Invalid option")

        print("Total Laundary Cost=Rs", self.l_bill, "\n")

    def sportsbill(self):
        print("******GAME MENU*******")

        print("1.Table tennis----->Rs 100", "2.Bowling----->Rs200", "3.Snooker--->Rs150", "4.Video games---->Rs500",
              "5.Pool--->Rs250", "6.Exit")

        while (1):

            g = int(input("Enter your choice:"))  # h=quantity

            if (g == 1):
                h = int(input("No. of hours:"))
                self.g_bill = self.g_bill + 100 * h

            elif (g == 2):
                h = int(input("No. of hours:"))
                self.g_bill = self.g_bill + 200 * h

            elif (g == 3):
                h = int(input("No. of hours:"))
                self.g_bill = self.g_bill + 150 * h

            elif (g == 4):
                h = int(input("No. of hours:"))
                self.g_bill = self.g_bill + 500 * h

            elif (g == 5):
                h = int(input("No. of hours:"))
                self.g_bill = self.g_bill + 250 * h
            elif (g == 6):
                break;

            else:

                print("Invalid option")

        print("Total Game Bill=Rs", self.g_bill, "\n")

    def display(self):
        print("******HOTEL BILL******")
        print("Customer details:")
        print("Customer name:", self.name)
        print("Customer address:", self.address)
        print("Check in date:", self.cindate)
        print("Check out date", self.coutdate)
        print("Room no.", self.rno)
        print("Your Room rent is:", self.r_rent)
        print("Your Food bill is:", self.f_bill)
        print("Your laundary bill is:", self.l_bill)
        print("Your Game bill is:", self.g_bill)

        self.ttl = self.r_rent + self.l_bill + self.g_bill + self.f_bill

        print("Your sub total bill is:", self.ttl)

        print("Your grandtotal bill is (18% GST INCLUSIVE):", self.ttl + (0.18 * self.ttl), "\n")
        self.rno += 1


def main():
    a = hotelcharge()

    while (1):
        print("1.Enter Customer Data")

        print("2.Calculate rommrent")

        print("3.Calculate restaurant bill")

        print("4.Calculate laundry bill")

        print("5.Calculate gamebill")

        print("6.Show total cost")

        print("7.EXIT")

        b = int(input("\nEnter your choice:"))
        if (b == 1):
            a.inputdetails()

        if (b == 2):
            a.roomrent()

        if (b == 3):
            a.restaurentbill()

        if (b == 4):
            a.laundrybill()

        if (b == 5):
            a.sportsbill()

        if (b == 6):
            a.display()

        if (b == 7):
            quit()


main()

