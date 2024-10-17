#Opens the file and reads it line by line
import meteor_data_class
import PySimpleGUI as sg
from meteor_data_class import MeteorDataEntry

def launchGUI(my_meteor1= None):
    # creating a meteor entry to be used later in the code(NEEDS TO BE OUTSIDE OF FOR LOOP SO DATA IS MAINTAINED AND NOT WRITEN OVER)
    my_meteor1 = MeteorDataEntry('', '', '', '', '3900000', '', '', '', '', '', '', '')

    # All the stuff inside your window.
    layout = [
                #This is the text field above the year input box
                [sg.Text('Years table')],
               #This is the actual year input box
                [sg.Multiline(default_text='Please enter the meteors that you want filtered by years here.', key = 'yearT', size=(None, 10))],
                #This is the text field above the mass input box
                [sg.Text('Mass table')],
        # This is the actual mass input box
                [sg.Multiline(default_text='Please enter the meteors that you want filtered by Mass here.', key = 'massT' ,size=(None, 10))],
        # This is where the user will be prompted to put in a year to filter through
                [sg.Text('Minimum Yer Limit (0 - 2022, exclusive): >'), sg.InputText(default_text = 0 ,key = 'yearU')],
        # This is where the user will be prompted to put in a mass to filter through
                [sg.Text('Minimum Mass Limit (grams, exclusive): >'), sg.InputText(default_text = 0 ,key = 'massU')],
        #These are the buttons at the bottom
                [sg.Button('Apply filters'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Filter Dataset Parameter Input', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event == 'Apply filters':

            yearLimit: int = values['yearU']
            massLimit: int = values['massU']
            yearinput: str = values['yearT']
            massinput: str = values['massT']

            # creating a meteor entry to be used later in the code(NEEDS TO BE OUTSIDE OF FOR LOOP SO DATA IS MAINTAINED AND NOT WRITEN OVER)
            my_meteor1 = MeteorDataEntry('', '', '', '', '3900000', '', '', '', '', '', '', '')

            # Go through all the Mass input, split the lines and the data and add the meteor to the mass table
            line = massinput.splitlines()

            # if there's no data in the line then it will break out of the while loop
            if not line:
                break

            # Taking a line and splitting it by the tab's and putting it into a variable to use
            for i in range(0, len(line)):
                x = line[i].split('\t', 11)

                # IMPORTANT need to see if the file line has all the meteor values
                while (len(x) < 12):
                    x.append('')

                # IMPORTANT need to create a Meteor Data Entry with the list of data read in from a file.
                newMeteor = MeteorDataEntry(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11])

                # Calling to add a meteor to the array
                my_meteor1.addMeatMass(newMeteor, yearLimit, massLimit, yearinput, massinput)

            line = yearinput.splitlines()

            # if there's no data in the line then it will break out of the while loop
            if not line:
                break

            # Taking a line and splitting it by the tab's and putting it into a variable to use
            for i in range(0, len(line)):
                x = line[i].split('\t', 11)

                # IMPORTANT need to see if the file line has all the meteor values
                while (len(x) < 12):
                    x.append('')

                # IMPORTANT need to create a Meteor Data Entry with the list of data read in from a file.
                newMeteor = MeteorDataEntry(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11])

                # Calling to add a meteor to the array
                my_meteor1.addMeatYear(newMeteor, yearLimit, massLimit, yearinput, massinput)
            # TBD ___________ Go through all the Year input, split the lines and the data and add the meteor to the year table
            # reuse lines 49 - 68 using the mass input data

            # prints the mass table
            my_meteor1.massTable()

            # prints the year table
            my_meteor1.yearTable()



    window.close()
#This runs the program
if __name__ == '__main__':
    launchGUI()