import numpy as np
from matplotlib import pyplot as plt
 
def polygon(n):
    print("Initializing x and y array of size "+str(n)+" for x and y co-ordinates")
    x=[None]*n
    y=[None]*n
 
    numberofleftturn=0
    numberofrightturn=0
    
    print("Getting Vertices:")
 
    for i in range (n): 
        x[i]=int(input("Enter x co-ordinate of Vertex "+str(i+1)+": "))
        y[i]=int(input("Enter y co-ordinate of Vertex "+str(i+1)+": "))
        plt.scatter(x[i],y[i])
 
    print("***************************************************")
    print("List of Vertices Before Sorting:")
    print("***************************************************")
    for i in range(n):
        print("("+str(x[i])+","+str(y[i])+")")
 
 
    print("Sorting All the Vertices in Counter Clockwise manner")
    center_point = [np.sum(x)/n, np.sum(y)/n]
    angles = np.arctan2(x-center_point[0],y-center_point[1])
    sort_tups = sorted([(i,j,k) for i,j,k in zip(x,y,angles)], key = lambda t: t[2],reverse=True)
    if len(sort_tups) != len(set(sort_tups)):
        raise Exception('You mistakenly input two equal vertices')
    x,y,angles = zip(*sort_tups)    
    
 
    print("***************************************************")
    print("List of Vertices after Sorting:")
    print("***************************************************")
    for i in range(n):
        print("("+str(x[i])+","+str(y[i])+")")
 
 
    print("***************************************************")
    print("Performing Turn Test:")
    print("***************************************************")
    
    print("Appending First Two Coordinate to the list of vertices")
    x = list(x)
    y = list(y)
    
    x.append(x[0])
    y.append(y[0])
 
    x.append(x[1])
    y.append(y[1])
 
    for i in range(n):
        print("At Point("+str(x[i+1])+","+str(y[i+1])+")")
        print("Points to consider: ("+str(x[i])+","+str(y[i])+")","("+str(x[i+1])+","+str(y[i+1])+")","("+str(x[i+2])+","+str(y[i+2])+")")
 
        turntest=(x[i+1]-x[i])*(y[i+2]-y[i])-(y[i+1]-y[i])*(x[i+2]-x[i])
        if(turntest>0):
            print("Left Turn")
            numberofleftturn=numberofleftturn+1
        elif(turntest<0):
            print("Right Turn")
            numberofrightturn=numberofrightturn+1
        else:
            print("Collinear")
 
    print("***************************************************")
    print("Checking Convexity:")
    print("***************************************************")
    if(numberofrightturn==0):
        if(numberofleftturn==0):
            print("All Points are Collinear")
        else:
            print("Polygon is a Convex Polygon")
 
    else:
        print("Polygon is a Concave Polygon")
 
    print("Plotting Co-ordinates")
    plt.plot(x,y,'-')
    
    print("Showing Graph")
    plt.show()
 
print("Implementation of Polygon, Turn Test, and Convexity")
print("***************************************************")
n=int(input("Enter no of Vertices:"))
polygon(n)
