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

        # This is to print the meteor class table
    def massTable(self):
        # Open a file for writing, have to use encoding because the data file has special characters, without this the program will crash.
        f = open("mass_filtered_data.txt", "w", encoding="utf-8")
        # for loop for all the values in the mass array to print out.
        for i in range(0, len(self.massArray)):
            f.write(f"{i+1:<5}{self.massArray[i].name:<24}{self.massArray[i].mass:<20}\n")
        f.close()

        # This prints the year table
    def yearTable(self):
        # Open a file for writing, have to use encoding because the data file has special characters, without this the program will crash.
        f = open("year_filtered_data.txt", "w", encoding="utf-8")
        # for loop for all the values in the year array to print out.
        for i in range(0, len(self.yearArray)):
            f.write(f"{i+1:<5}{self.yearArray[i].name:<24}{self.yearArray[i].year:<20}\n")
        f.close()


    #this adds the Meteor's into the self.MeteorArray
    def addMeat(self, meteor,yearLimit,massLimit,yearinput,massinput):
        #will put read the meteor and put it into the array
        self.meteorArray.append(meteor)

        #  check the length of the value before trying to use it to prevent error
        #  meteor being sent in is a list of the data.  It is not a MeteorDataEntry that you can reference the attributes of
        if len(meteor.mass) >=1:
           #if the meteor's mass is in the > 2900000 then add it to massArray
           if float(meteor.mass) >= float(massLimit):
             self.massArray.append(meteor)
        # if the meteor's year is greater than or equal to  2013 then add to the yearArray
        if len(meteor.year) >= 1:
           if int(meteor.year) >= int(yearLimit):
             self.yearArray.append(meteor)

        # this adds the Meteor's into the self.MeteorArray

    # NEW - add the meteor to the mass table
    def addMeatMass(self, meteor, yearLimit, massLimit, yearinput, massinput):
        # will put read the meteor and put it into the array
        self.meteorArray.append(meteor)

        #  check the length of the value before trying to use it to prevent error
        #  meteor being sent in is a list of the data.  It is not a MeteorDataEntry that you can reference the attributes of
        if len(meteor.mass) >= 1:
            # if the meteor's mass is in the > 2900000 then add it to massArray
            if float(meteor.mass) >= float(massLimit):
                self.massArray.append(meteor)

    # NEW - Add the meteor to the year table
    def addMeatYear(self, meteor, yearLimit, massLimit, yearinput, massinput):
        # will put read the meteor and put it into the array
        self.meteorArray.append(meteor)

        # if the meteor's year is greater than or equal to  2013 then add to the yearArray
        if len(meteor.year) >= 1:
            if int(meteor.year) >= int(yearLimit):
                self.yearArray.append(meteor)

