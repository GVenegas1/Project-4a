# project-4a

# Author: Gabriel Venegas
# GitHub username: GVenegas1
# Date: 10/22/2025
# Description: Calculate the distance in meters an object fall due to
# gravity over a given time. Using the formula: d = (1/2) * g * t^2
# where g = 9.8 m/s and t is time in seconds


def fall_distance(t):

    """Calculate the distance an object falls due to gravity in a given time. \n

    t (float) = Time in seconds that the object has been falling.\n

    Returns : distance in meters that the object has fallen """

    g = 9.8 #gavity (m/s^2)
    d = 0.5 * g * (t ** 2) #apply formula [(1/2) * gravity * time^2]
    return d    #return distance

#test function
#dist = fall_distance(3.2)
#print(dist)