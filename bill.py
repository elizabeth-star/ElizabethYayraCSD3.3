class elecBill:
    vat = 0.1250
    natElecL = 0.0200
    striL = 0.0300
    nhilGet = 0.0500
    serCharg = 0.4075
    montBill = {}

    def __init__(self, unitPrice):
        self.unitPrice = 0.7979

    def meterRead(self):
    
        if cur > prev:
            metread = cur - prev
            print(metread, 'kWh')

        else:
            return

    def monthBill(self):
        self.montBill = round((metread * self.unitPrice),3)
        print('Bill is: ', self.montBill)

    def vatR(self):
        vaR = ((cur - prev) * self.unitPrice)
        self.va = round((self.vat * ((32*self.serCharg) + vaR)),2)
        print('Vat on bill: ', self.va)
    def natElecLe(self):
        nat = ((cur - prev) * self.unitPrice)
        self.natElec = round((self.natElecL * nat),2)
        print('National Electr. Levy: ', self.natElec)
    def striLi(self):
        light = ((cur - prev) * self.unitPrice)
        self.striLii = round((self.striL * light),2)
        print('street Light: ', self.striLii)
    def nhilGetF(self):
        get = ((cur - prev) * self.unitPrice)
        self.nhilGe = round((self.nhilGet * ((32*self.serCharg) + get)),2)
        print('NHIS and GETFUND Levy: ', self.nhilGe)
    def servChar(self):
        servCha = round((32 * self.serCharg),2)
        print('Service charges for 32days: ', servCha)
    def totalThisMonth(self):
       
        totalThisMont = round(((self.montBill) + (32 * self.serCharg) + ((self.montBill + (32 * self.serCharg)) * self.nhilGet) + (self.montBill * self.striL) + 
                                (self.montBill * self.natElecL) + (((self.montBill + (32 * self.serCharg)) * self.vat))),3)
        print('Total current bill: ', totalThisMont)


    
    def elecCal(self):
        
        choice = eval(input('choose 1: monthly calcuation \n2: other services \nEnter: '))
        if choice == 1:
            d.meterRead()
            d.monthBill()
            d.vatR()
            d.natElecLe()
            d.striLi()
            d.nhilGetF()
            d.servChar()
            d.totalThisMonth()
        elif choice == 2:
            choose = eval(input('1: NHIS and GETFUND \n2: Service charges \n3: Value Added Tax(VAT) \n4: Meter Readings \n5: Stright Light \n6: National Electrification Levy \n7: This Month Bill \n Enter: '))
            if choose ==1:
                d.nhilGetF()
            elif choose ==2:
                d.servChar()
            elif choose ==3:
                d.vatR()
            elif choose == 4:
                d.meterRead()
            elif choose == 5:
                d.striLi()
            elif choose == 6:
                d.natElecLe()
            else:
                print('Wrong selection.')
                    
            
            
            
        else:
            print('start again.')

print('Electricity bill calculation.')
prev = eval(input('Enter previous meter readings: '))
cur = eval(input('Enter current meter readings: '))
metread = cur - prev
d = elecBill(0.7979)

d.elecCal()
