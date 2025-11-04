def solve(N: int, X: list[float], Y: list[float]) -> float:
    import math
    import sys
    """
    Return the area of the rectangle described by the given points.
    
    N: the number of given points
    X: a list containing the x-coordinate of each point
    Y: a list containing the y-coordinate of each point
    """
    # YOUR CODE HERE

    # finding the sum for each components
    sumX = 0
    sumY = 0
    for i in X:
        sumX += i
    for j in Y:
        sumY += j
    
    # now finding the the center/avg of each axis along the paramenters
    avgX, avgY = sumX/15,sumY/15
    
    # finding the corresponding radians for 33 deg

    rad = math.radians(33)
    X_axis = math.cos(rad)
    Y_axis = math.sin(rad)

# now I will project points onto the rotated axis
    proj_x = []
    proj_y = []
    # recentring each point 
    for x,y in zip(X,Y):
        dx = x - avgX
        dy = y - avgY
    # projecting on x axis and y axis
        proj_on_x = dx * X_axis + dy * Y_axis
        proj_on_y = -dx * Y_axis + dy * X_axis

        # append each point to the lists
        proj_x.append(proj_on_x)
        proj_y.append(proj_on_y)

    # find the width and height
    width = max(proj_x)- min(proj_x)
    height = max(proj_y) - min(proj_y)

    # return area
        
    return width*height

    return 0.0


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        X, Y = zip(*(map(int, input().split()) for _ in range(N)))
        X = int(X)
        Y = int(Y)
        print(solve(N, X, Y))


if __name__ == '__main__':
    main()
