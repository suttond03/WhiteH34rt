import time
import os


title = 'WhiteH34rt'
universalInput=[]
date=time.strftime('%m/%d/%Y %H:%M:%S')

#Options
homeoptions = ['(1) Person-Files', '(2) OSINT', '(3) Incidents', '(4) Search', '(5) Dev']

#PERSONS FILES
personFiles = ['(1) New-Person', '(2) New-HighRisk-Person', '(3) Site']

#OSINT
osint = ['This is the OSINT directory...']

#INCIDENTS
incidents = ['(1) New-Incident', '(2) View-Incidents']


#Functions

def display(options):
    print(title)
    print("-------------")
    print(options)
def usrinput():
    count = 0
    while count < 2:
        userinput = int(input('Enter Value: '))
        if userinput <= 3 and userinput >= 1:
            universalInput.append(userinput)
            break
        else:
            count += 1
def personFile():
    #General#
    firstname=input('Enter First Name: ')
    lastname=input('Enter Last Name: ')
    dob = input("Enter Date of Birth: ")
    address = input("Enter Address: ")
    phone = input("Enter Phone Number: ")
    citizenship = input("Enter citizenship: ")
    occupation = input("Enter Occupation: ")

    #Physical Desc#
    race = input("Enter Race: ")
    sex = input("Enter Sex: ")
    height = input("Enter Height: ")
    weight = input("Enter Weight: ")
    hair_color = input("Enter Hair Color: ")
    skin_tone = input("Enter Skin Tone: ")
    eye_color = input("Enter Eye Color: ")

    #Comments#
    comments=input('Enter Additional Comments: ')

    #Functions
    directory='Files/PersonFiles/'+str(lastname)
    os.mkdir(directory)
    file=directory+'/'+firstname+'.txt'
    f=open(str(file), 'w')
    f.write("PROFILE")
    f.write("\n")
    f.write("\n")
    f.write("Name: " + str(firstname)+' '+str(lastname))
    f.write("\n")
    f.write("Index Date: " + date)
    f.write("\n")
    f.write("Date of Birth: " + dob)
    f.write("\n")
    f.write("Address: " + address)
    f.write("\n")
    f.write("Phone #: " + phone)
    f.write("\n")
    f.write("Citizenship: " + citizenship)
    f.write("\n")
    f.write("Occupation: " + occupation)
    f.write("\n")
    f.write("\n")
    f.write("\n")
    f.write("\n")
    f.write("PHYSICAL DESC")
    f.write("\n")
    f.write("\n")
    f.write("Race: " + race)
    f.write("\n")
    f.write("Sex: " + sex)
    f.write("\n")
    f.write("Height: " + height)
    f.write("\n")
    f.write("Weight: " + weight)
    f.write("\n")
    f.write("Hair Color: " + hair_color)
    f.write("\n")
    f.write("Skin Tone: " + skin_tone)
    f.write("\n")
    f.write("Eye Color: " + eye_color)
    f.write("\n")
    f.write("\n")
    f.write("\n")
    f.write("\n")
    f.write("ADDITIONAL")
    f.write("\n")
    f.write("\n")
    f.write("Comments: " + comments)
    f.close()
def highriskpersonfile():
    #General
    print('General-Info')
    firstname = input("Enter Person First Name:")
    lastname=input('Enter Person Last Name: ')
    dob = input("Enter Date of Birth:")
    address = input("Enter Address:")
    phone = input("Enter Phone Number:")
    citizenship = input("Enter citizenship:")

    #Physical Desc
    print("Physical-Description")
    race = input("Enter Race:")
    sex = input("Enter Sex:")
    height = input("Enter Height:")
    weight = input("Enter Weight:")
    hair_color = input("Enter Hair Color:")
    skin_tone = input("Enter Skin Tone:")
    eye_color = input("Enter Eye Color:")

    #Education
    print("Education")
    school = input("Enter School:")
    year = input("Enter Education Level:")

    #Occupation
    print("Occupation")
    title = input("Enter Occupation Details:")

    #Socials
    print("Socials")
    insta = input("Enter Instagram Handle:")
    snap = input("Enter Snapchat Handle:")
    twit = input("Enter Twitter Handle:")
    other = input("Enter Other:")

    #Vehicle#
    print("Vehicle")
    make = input("Enter Car Make:")
    model = input("Enter Car Model:")
    vin = input("Enter VIN #:")


    ##Write to File##
    directory='Files/HighRisk-PersonFiles/'+str(firstname + lastname)+'.txt'
    f=open(directory, 'w')
    f.write("PROFILE")
    f.write("\n")
    f.write("\n")
    f.write("Name: " + str(firstname)+' '+str(lastname))
    f.write("\n")
    f.write("Index Date: " + date)
    f.write("\n")
    f.write("Date of Birth: " + dob)
    f.write("\n")
    f.write("Address: " + address)
    f.write("\n")
    f.write("Phone #: " + phone)
    f.write("\n")
    f.write("Citizenship: " + citizenship)
    f.write("\n")
    f.write("\n")
    f.write("\n")
    f.write("\n")
    f.write("PHYSICAL DESC")
    f.write("\n")
    f.write("\n")
    f.write("Race: " + race)
    f.write("\n")
    f.write("Sex: " + sex)
    f.write("\n")
    f.write("Height: " + height)
    f.write("\n")
    f.write("Weight: " + weight)
    f.write("\n")
    f.write("Hair Color: " + hair_color)
    f.write("\n")
    f.write("Skin Tone: " + skin_tone)
    f.write("\n")
    f.write("Eye Color: " + eye_color)
    f.write("\n")
    f.write("\n")
    f.write("\n")
    f.write("\n")
    f.write("EDUCATION")
    f.write("\n")
    f.write("\n")
    f.write("School: " + school)
    f.write("\n")
    f.write("Year: " + year)
    f.write("\n")
    f.write("Other: ")
    f.write("\n")
    f.write("\n")
    f.write("\n")
    f.write("\n")
    f.write("OCCUPATION")
    f.write("\n")
    f.write("\n")
    f.write("Title: " + title)
    f.write("\n")
    f.write("\n")
    f.write("\n")
    f.write("\n")
    f.write("SOCIALS")
    f.write("\n")
    f.write("\n")
    f.write("Instagram Handle: " + insta)
    f.write("\n")
    f.write("Snapchat Handle: " + snap)
    f.write("\n")
    f.write("Twitter: " + twit)
    f.write("\n")
    f.write("Other: " + other)
    f.write("\n")
    f.write("\n")
    f.write("\n")
    f.write("\n")
    f.write("VEHICLE")
    f.write("\n")
    f.write("\n")
    f.write("Make: " + make)
    f.write("\n")
    f.write("Model: " + model)
    f.write("\n")
    f.write("VIN #: " + vin)
    f.close()
def site():
    #General
    type = input("Site Type:")
    owner = input("Site Owner:")
    line1 = str(input("Address Line 1:"))
    line2 = input("Address Line 2:")
    state = input("State:")
    zipcode = input("Zipcode:")

    #Functions
    directory='Files/Sites/'+str(line1)
    os.mkdir(directory)
    file=directory+'/'+line1+'.txt'
    f=open(file, 'w')
    f.write("SITE")
    f.write("\n")
    f.write("\n")
    f.write("Site Type: " + type)
    f.write("\n")
    f.write("Site Owner: " + owner)
    f.write("\n")
    f.write("Street Address: " + line1 + " " + line2)
    f.write("\n")
    f.write("State: " + state)
    f.write("\n")
    f.write("Zipcode: " + zipcode)
    f.write("\n")
    f.write("Coordinates: ")
    f.write("\n")
    f.write("\n")
    f.write("\n")
    f.write("\n")
    f.write("Index Date: " + date)
    f.close()
def newincident():
    #General
    name=input('Enter Incident Nickname: ')
    type=input('Enter Incident Type: ')
    location=input('Enter Incident Location: ')
    associates=input('Enter Incident Associates: ')
    debrief=input('Enter Brief Explanation of Incident: ')
    comments=input('Enter Additional Comments: ')

    #Functions
    directory='Files/Incidents/incidents.txt'
    f=open(directory, 'a')
    f.write("""
                    ~{INCIDENT}~ """+name+"""          Indexed: """+date+"""
                        Location: """+location+"""
                        Associates: """+associates+"""
                        Debrief: """+debrief+"""


                        Additional-Comments: """+comments)
    f.write('\n')
    f.close()
    print("""
                    ~{INCIDENT}~ """+name+"""          Indexed: """+date+"""
                        Location: """+location+"""
                        Associates: """+associates+"""
                        Debrief: """+debrief+"""


                        Additional-Comments: """+comments)
def viewincidents():
    f=open('Files/Incidents/incidents.txt', 'r')
    print(f.readlines())

def search():
    print()
def dev():
    print()

#Control Flow
display(homeoptions)
usrinput()


if universalInput[-1] == 1:
    display(personFiles)
    usrinput()
    #Persons Files Options
    if universalInput[-1] == 1:
        personFile()
    elif universalInput[-1] == 2:
        highriskpersonfile()
    elif universalInput[-1] == 3:
        site()
elif universalInput[-1] == 2:
    display(osint)
    usrinput()
    #OSINT Options
elif universalInput[-1] == 3:
    display(incidents)
    usrinput()
    #Incidents Options
    if universalInput[-1] == 1:
        newincident()
    elif universalInput[-1] == 2:
        viewincidents()
elif universalInput[-1] == 4:
    search()