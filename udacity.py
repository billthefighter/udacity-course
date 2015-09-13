# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    x = init[0]
    y = init[1]
    g=0
    open = [[g, x, y]]
    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand
    while not found and not resign:
        #print len(open)
        if len(open) == 0: #check fo corner case where no more elements can be found
            #print"fart"
            resign = True
            print closed[:][0]
            print closed[:][1]
            print closed[:][2]
            print closed[:][3]
            return "fail"
        else:
            #print "pop"
            open.sort()    #open sort list
            open.reverse() #flip open list so item with lowest value is highest
            next = open.pop() # pop lowest value off list
            x = next[1]
            y = next[2]
            g = next[0]

            if x == goal[0] and y == goal[1]:
                found = True
                print closed[:][0]
                print closed[:][1]
                print closed[:][2]
                print closed[:][3]
            for i in xrange(0,len(delta)):
                move = [x + delta[i][0], y + delta [i][1]] #apply the delta to popped open list element and save as move
                #print move
                if move[0] >= 0 and move[0] < len(grid) and move[1] >= 0 and move[1] < len(grid[0]): #check if move puts robot out of bounds
                    #print "checked"
                    x2=move[0]
                    y2=move[1]
                    #print closed
                    if closed[x2][y2] == 0 and grid[x2][y2] == 0: #if it's not closed and a valid move, do this
                        #print move
                        #print "passed check"
                        g2 = g + cost
#                        x2=move[0]
#                        y2=move[1]
                        open.append([g2,x2,y2])
                        closed[x2][y2] = 1
                        #print next   
                    pass
    return next


print search(grid,init,goal,cost)
