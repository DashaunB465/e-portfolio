
#do not accept any negative numbers, round to 2 decimal places
def main():
    print("Welcome to Merlin's Pet Grooming!\n")
    print("For a proper invoice we will need the customer and pet' information.")
    print("We can start with customer.\n")

    # get customer info
    CN = input("Customer' First and Last name? ")
    CA = input("Customer' Address? ")
    CP = input("Please enter all 9 digits as followed: 123-123-1234\nCustomer' Phone number? ")
    CE = input("Customer' Email? ")
    
    # get pet info
    print("\nNow for the Pet.")
    PN = input("Pet' Name? ")
    PT = input("Let's keep things simple by entering the pet type as followed: cat, dog, bird, etc.\nPet Type? ")

    # error check for invalid age
    PA = int(input("If pet is only months or days old input 1 as default.\nPlease enter age in completed years.\nPet Age? "))
    valid = False
    while PA < 1:
        PA= int(input("Sorry! that input is invalid. Enter age in postitive whole numbers only.\nPet Age? "))
    else:
        valid = True
        
    # call the object reference for Customer and pet, store info given by user
    new_Customer = Customer(CN,CA,CP,CE)
    new_Pet = Pet(PN,PT,PA)

    # get grooming info
    # call the object reference for Service
    print("\nCustomer, Pet, and Services will displayed below.")
    new_Service = Service("Bath","Hair Trim","Clipped Nails",7,4.50,2.25)
    
    # display complete invoice
    print("\n*** INVOICE COMPLETE. ***")
    print(new_Customer)
    print(new_Pet)
    print(new_Service)
    new_Service.sub_total()
    new_Service.tax()
    new_Service.total()
    new_Service.display()
    print()
    input("Press enter to exit....")
    
# Customer class
class Customer:
    # private varibles and atributes
    __Name = ""
    __Address = ""
    __Phone = ""
    __Email = ""

    # default constructer
    def __init__(self, Name, Address, Phone, Email ):
        self.__Name = Name
        self.__Address = Address
        self.__Phone = Phone
        self.__Email = Email

    # string method needed to print class atributes:
    def __str__(self):
        return "\n-----Customer-----\nName: "+ self.__Name +"\nAddress: "+ self.__Address +"\nPhone: "+ self.__Phone +"\nEmail: "+ self.__Email
        
    # setters and getters for varibles
    #Name:
    def set_name(self, n):
        self.__Name = n
        print("\nCustomer' name changed to: " + self.__Name)
    def get_name(self):
        print("\nCustomer' name is: " + self.__Name)
        return self.__Name

    #Adrress:
    def set_address(self, a):
        self.__Address = a
        print("\nCustomer' address changed to: " + self.__Address)
    def get_address(self):
        print("\nCustomer' address is: " + self.__Address)
        return self.__Address

    #Phone:
    def set_phone(self, p):
        self.__Phone = p
        print("\nCustomer' phone changed to: " + self.__Phone)
    def get_phone(self):
        print("\nCustomer' phone is: " + self.__Phone)
        return self.__Phone
    
    #Email
    def set_email(self, e):
        self.__Email = e
        print("\nCustomer' email changed to: " + self.__Email)
    def get_email(self):
        print("\nCustomer' email is: " + self.__Email)
        return self.__Email

# Pet class
class Pet:
    # private varibles and atributes
    __PName = ""
    __PType = ""
    __PAge = 0
    
    # default constructer
    def __init__(self, p_name, p_type, p_age):
        self.__PName = p_name
        self.__PType = p_type
        self.__PAge = p_age

    # string method needed to print class atributes:
    def __str__(self):
        return "\n-------Pet-------\nName: " + self.__PName +"\nType: " + self.__PType + "\nAge: " + str(self.__PAge)

    # setters and getters for varibles
    #Name:
    def set_petname(self, pn):
        self.__PName = pn
        print("\nPet' name changed to: " + self.__PName)
    def get_petname(self):
        print("\nPet' name is: " + self.__PName)
        return self.__PName

    #Type:
    def set_pettype(self, pt):
        self.__PTpye = pt
        print("\nPet' type changed to: " + self.__PType)
    def get_pettype(self):
        print("\nPet' type is: " + self.__PType)
        return self.__PType

    #Age:
    def set_petage(self, pa):
        self.__PAge = pa
        print("\nPet' age changed to: " + str(self.__PAge))
    def get_petage(self):
        print("\nPet' age is: " + str(self.__PAge))
        return self.__PAge

# Grooming/Price class
class Service:
    # private varibles and atributes
    __Serv1 = ""
    __serv2 = ""
    __Serv3 = ""
    __Charge1 = 0
    __Charge2 = 0
    __Charge3 = 0
    subTotal = 0
    tax = 0
    SALES_TAX = 0.0975
    total_charges = 0
    
    # default constructer
    def __init__(self, s1, s2, s3, c1, c2, c3):
        self.__Serv1 = s1
        self.__Serv2 = s2
        self.__Serv3 = s3
        # add if for error check for 0 and negative inputs
        if c1 >= 1:
            self.__Charge1 = c1
        else:
            self.__Charge1 = 0
        if c2 >= 1:
            self.__Charge2 = c2
        else:
            self.__Charge2 = 0
        if c3 >= 1:
            self.__Charge3 = c3
        else:
            self.__Charge3 = 0
        

    # string method needed to print class atributes:
    def __str__(self):
        return "\n-----Service-----\n" + self.__Serv1 + "\t\t$" + format(self.__Charge1,",.2f") +"\n"+ self.__Serv2 + "\t$" + format(self.__Charge2,",.2f") + "\n" + self.__Serv3 + "\t$" + format(self.__Charge3,",.2f")

    # no setters or getters
    # prices and services will not be changed after inserted into obj reference

    # calculate services
    def sub_total(self):
        self.subTotal = self.__Charge1 + self.__Charge2 + self.__Charge3

    def tax(self):
        self.tax = self.subTotal * self.SALES_TAX

    def total(self):
        self.total_charges = self.tax + self.subTotal

    # display
    def display(self):
        print("\n\nSub Total\t\t$" + format(self.subTotal,",.2f"))
        print ("Tax\t\t\t $" + format(self.tax,",.2f"))
        print("Total\t\t\t$" +format(self.total_charges,",.2f"))

#call main
main()
