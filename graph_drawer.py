import matplotlib.pyplot as plt

def main(): #Mainly ploting, creating the graph

    introduction()
    inputs, name,  timestype, valuetype = getuserinputs()  #Return the dict 'inputs' with provided user times, values inputs and the name of the graph
    sorted_times = sorted(inputs.keys()) #Sorting out day in an increasing order incase out of order
    sorted_values = [inputs[time] for time in sorted_times]
    for i in range(1, len(sorted_times)): #Visual indications of the flutuation of the value over time
        if sorted_values[i] > sorted_values[i-1]:
            plt.plot(sorted_times[i-1:i+1], sorted_values[i-1:i+1], marker='o', color='green') #If the later point is higher the line connecting will be green
        else:
            plt.plot(sorted_times[i-1:i+1], sorted_values[i-1:i+1], marker='o', color='red') #If the later point is lower the line connecting will be red

    if len(sorted_times) == 1: #Avoid plot error if there is only one point
        plt.plot(sorted_times, sorted_values, 'bo')

    plt.xlabel(timestype) #Labeling the x axis and y axis and the title
    plt.ylabel(valuetype)
    plt.title(name) #Give the graph a name from user input
    plt.grid(True)
    plt.show()

def introduction(): #Start of the program
    print("Line Graph Drawer 1.0 Created By Pham Ngoc Thanh ")
    print("This program helps you create a graph to represent the changes of a value you provided over time!")
    print("Year 2016 30.74$\nYear 2018 28.4$\nYear 2020 30$\nYear 28 28$")
    print("As you can see, you do not need to provide every single day in the period.")
    print("Let's start!")

def getuserinputs():
    inputs = {}  #Dict storing time and value
    name = input("Enter the name of the linegraph(example:Line Graph of Casio WR100M Watch over Year) :") #Use to name the graph
    timestype = input("Enter a unit of time(example: second/hour/day/year): ") #Use to label the x axis
    valuetype = input("Enter the type of the value(example: $/vnđ/people(s)/user(s)): ") #Use to label the y axis
    while(1):
        times = input("Enter the list of " + str(timestype) + "s(example: 1 6 19 28): ").split() #Get a valid list of time to use as keys in the 'inputs' dict
        try:
            times = list(map(int,times))
            break
        except ValueError:
            print("Invalid days inputs, please try again!") #Make sure inputs are valid
    for time in times:
        while(1):
            value = input("Enter the value from " + str(timestype) + " " + str(time) + ": ") #Assign a value to each listed time
            try:
                value = float(value)
                inputs[time] = value
                break
            except ValueError:
                print("Invalid value input, please try again!") #Make sure inputs are valid
    return inputs, name, timestype, valuetype

main()