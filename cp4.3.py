import random
import matplotlib.pyplot as plt
import numpy

# This is the main function which tries to integrate everything
def main():

    # I've taken input from user the number of iterations and length of the road
    roadlength = int(input("Enter road length: "))
    numOfiterations = int(input("Enter number of iterations:"))
    sum = 0
    a_speed = [0]*roadlength
    density = [0]*roadlength

    for i in range(roadlength):
        d = float(i)/(roadlength)
        for j in range(numOfiterations):
            # this basically adds up all steady counts, then average is taken after loop
            # 'count' and 'random_array' are the functions called. The 'move' function is called inside 'count' function
            sum = sum + count(random_array(roadlength,i))
        # so according to the question avg speed is number of cars moved/total number of cars so....
        if (i==0):
            avg_speed = 0
        else:
            avg_speed = sum/(roadlength*i)
        
        a_speed[i]= avg_speed
        density[i] = d
    plt.plot(density,a_speed)  
    plt.xlabel("Car Density")
    plt.ylabel("Average speed")
    plt.show()      
        
        

# This function returns the steady count(for steady speed)
def count(generatedarray):

    b =0 
    while(True):
        # Move function is called which will return a count
        # I've made this change, I now assign cars(which is the changed array from move function) to generatedarray 
        a,cars = move(generatedarray)
        generatedarray = cars
        if(a==b):
            # This returns a steady count
            return a
        b=a        

# This function moves the cars and returns the count (number of cars moved)
def move(anarray):
    cars = anarray 
    count = 0
    for j in range(len(cars)):
        if cars[j]==1:
            if(j < len(cars) -1):
                if cars[j+1] == 0:
                    cars[j+1] = 1
                    cars[j] = 0
                    count = count + 1
            else:
                if cars[0]==0:
                    cars[j]=0
                    cars[0]=1  
                    count = count + 1            

    # this returns the moved array cars 
    print(cars)
    return (count,cars)

# This function generates a random array by taking number of cars and size of road
def random_array(roadsize, numOfcars):
    arr = [ 0 for i in range(roadsize) ]
    counter = 0
    while counter < numOfcars:
        random_index = random.randint(0, roadsize - 1)
        if arr[random_index] != 1:
            arr[random_index] = 1
            counter += 1
    return arr        

if __name__ == "__main__":
         main()   
            
