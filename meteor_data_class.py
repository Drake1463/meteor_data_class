#This the Meteor class
class MeteorDataEntry:
    def __init__(self,name, id ,nametype,recclass,mass,fall, year,recclat, reclong ,geolocation, states, counties):
        #This is the attributes being read in.
        self.name = name
        self.id = id
        self.nametype = nametype
        self.recclass= recclass
        self.mass = mass
        self.fall = fall
        self.year = year
        self.recclat = recclat
        self.reclong = reclong
        self.geolocation = geolocation
        self.states = states
        self.counties = counties
        self.meteorArray =[]
        self.massArray = []
        self.yearArray = []

    #This is to print the meteor class table
    def massTable(self):
        #Label for  the table with a string called name
        name_label = 'NAME'
        # Label for  the table with a string called mass
        mass_label = 'MASS (g)'
        # print the labels with spacing
        print(f"     {name_label:<24}{mass_label:<20}")
        #print the seperater
        print("============================================")
        #for loop for all the values in the mass array to print out.
        for i in range(0, len(self.massArray)):
            print(f"{i:<5}{self.massArray[i].name:<24}{self.massArray[i].mass:<20}")

    #This prints the year table
    def yearTable(self):
        # Label for  the table with a string called name
        name_label = 'NAME'
        # Label for  the table with a string called year
        year_label = 'YEAR'
        # print 5 blank lines to seperate the tables
        print('\n\n\n\n\n')
        #labels
        print(f"     {name_label:<24}{year_label:<20}")
        # print the title bar seperator
        print("============================================")
        # for loop for all the values in the year array to print out.
        for i in range(0,len(self.yearArray)):
            print(f"{i:<5}{self.yearArray[i].name:<24}{self.yearArray[i].year:<20}")

    #this adds the Meteor's into the self.MeteorArray
    def addMeat(self, meteor):
        #will put read the meteor and put it into the array
        self.meteorArray.append(meteor)

        #  check the length of the value before trying to use it to prevent error
        #  meteor being sent in is a list of the data.  It is not a MeteorDataEntry that you can reference the attributes of
        if len(meteor.mass) >=1:
           #if the meteor's mass is in the > 2900000 then add it to massArray
           if float(meteor.mass) >= float(2900000):
             self.massArray.append(meteor)
        # if the meteor's year is greater than or equal to  2013 then add to the yearArray
        if len(meteor.year) >= 1:
           if int(meteor.year) >= int(2013):
             self.yearArray.append(meteor)



