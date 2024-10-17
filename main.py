#Opens the file and reads it line by line
import meteor_data_class
from meteor_data_class import MeteorDataEntry

#reading the files of meteors
def definers_file():
    #Opens the file and reads
    f=open("Text.txt",'r')

    #creating a meteor entry to be used later in the code(NEEDS TO BE OUTSIDE OF FOR LOOP SO DATA IS MAINTAINED AND NOT WRITEN OVER)
    my_meteor1 = MeteorDataEntry('', '', '', '', '3900000', '', '', '', '', '', '', '')

    #A count of the line that is read in.
    count = 0

    #IMPORTANT: Need to read first line and throw out because it is the header
    line = f.readline()

    while True:
        count +=1
        #Actually reads in a line from the file
        line = f.readline()

        # if there's no data in the line then it will break out of the while loop
        if not line:
            break

        # remove end of line character from the line read in
        line = line.strip('\n')

        #Taking a line and splitting it by the tab's and putting it into a variable to use
        x = line.split('\t', 11)
 
        # IMPORTANT need to see if the file line has all the meteor values
        while(len(x) < 12):
            x.append('')

        # IMPORTANT need to create a Meteor Data Entry with the list of data read in from a file.
        newMeteor = MeteorDataEntry(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8],x[9],x[10], x[11])

        #Calling to add a meteor to the array
        my_meteor1.addMeat(newMeteor)

    #Closes the files so we save memory
    f.close()

    # prints the mass table
    my_meteor1.massTable()

    # prints the year table
    my_meteor1.yearTable()

#This runs the program
if __name__ == '__main__':
    #Calls to read the file
    definers_file()

