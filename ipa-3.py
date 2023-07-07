'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    if from_member in social_graph[to_member]["following"] and to_member in social_graph[from_member]["following"]:
        return "friends"
    elif from_member in social_graph[to_member]["following"]:
        return "followed by"
    elif to_member in social_graph[from_member]["following"]:
        return "follower"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    b=board #shortened cuz lazy to type!

    try:
        if len(b)==3:
            bcheck=[
                #horizontal
                [b[0][0],b[0][1],b[0][2]],
                [b[1][0],b[1][1],b[1][2]],
                [b[2][0],b[2][1],b[2][2]],

                #vertical
                [b[0][0],b[1][0],b[2][0]],
                [b[0][1],b[1][1],b[2][1]],
                [b[0][2],b[1][2],b[2][2]],

                #diagonal
                [b[0][0],b[1][1],b[2][2]],
                [b[2][0],b[1][1],b[0][2]]
            ]
            
            xchar=["X","X","X"]
            ochar=["O","O","O"]

        elif len(b)==4:
            bcheck=[
                #horizontal
                [b[0][0],b[0][1],b[0][2],b[0][3]],
                [b[1][0],b[1][1],b[1][2],b[1][3]],
                [b[2][0],b[2][1],b[2][2],b[2][3]],
                [b[3][0],b[3][1],b[3][2],b[3][3]],
                
                #vertical
                [b[0][0],b[1][0],b[2][0],b[3][0]],
                [b[0][1],b[1][1],b[2][1],b[3][1]],
                [b[0][2],b[1][2],b[2][2],b[3][2]],
                [b[0][3],b[1][3],b[2][3],b[3][3]],

                #diagonal
                [b[0][0],b[1][1],b[2][2],b[3][3]],
                [b[3][0],b[2][1],b[1][2],b[0][3]]
            ]
            
            xchar=["X","X","X","X"]
            ochar=["O","O","O","O"]

        elif len(b)==5:
            bcheck=[
                #horizontal
                [b[0][0],b[0][1],b[0][2],b[0][3],b[0][4]],
                [b[1][0],b[1][1],b[1][2],b[1][3],b[1][4]],
                [b[2][0],b[2][1],b[2][2],b[2][3],b[2][4]],
                [b[3][0],b[3][1],b[3][2],b[3][3],b[3][4]],
                [b[4][0],b[4][1],b[4][2],b[4][3],b[4][4]],
                
                #vertical
                [b[0][0],b[1][0],b[2][0],b[3][0],b[4][0]],
                [b[0][1],b[1][1],b[2][1],b[3][1],b[4][1]],
                [b[0][2],b[1][2],b[2][2],b[3][2],b[4][2]],
                [b[0][3],b[1][3],b[2][3],b[3][3],b[4][3]],
                [b[0][4],b[1][4],b[2][4],b[3][4],b[4][4]],

                #diagonal
                [b[0][0],b[1][1],b[2][2],b[3][3],b[4][4]],
                [b[4][0],b[3][1],b[2][2],b[1][3],b[0][4]]
            ]
            
            xchar=["X","X","X","X","X"]
            ochar=["O","O","O","O","O"]

        elif len(b)==6:
            bcheck=[
                #horizontal
                [b[0][0],b[0][1],b[0][2],b[0][3],b[0][4],b[0][5]],
                [b[1][0],b[1][1],b[1][2],b[1][3],b[1][4],b[1][5]],
                [b[2][0],b[2][1],b[2][2],b[2][3],b[2][4],b[2][5]],
                [b[3][0],b[3][1],b[3][2],b[3][3],b[3][4],b[3][5]],
                [b[4][0],b[4][1],b[4][2],b[4][3],b[4][4],b[4][5]],
                [b[5][0],b[5][1],b[5][2],b[5][3],b[5][4],b[5][5]],
                
                #vertical
                [b[0][0],b[1][0],b[2][0],b[3][0],b[4][0],b[5][0]],
                [b[0][1],b[1][1],b[2][1],b[3][1],b[4][1],b[5][1]],
                [b[0][2],b[1][2],b[2][2],b[3][2],b[4][2],b[5][2]],
                [b[0][3],b[1][3],b[2][3],b[3][3],b[4][3],b[5][3]],
                [b[0][4],b[1][4],b[2][4],b[3][4],b[4][4],b[5][4]],
                [b[0][5],b[1][5],b[2][5],b[3][5],b[4][5],b[5][5]],

                #diagonal
                [b[0][0],b[1][1],b[2][2],b[3][3],b[4][4],b[5][5]],
                [b[5][0],b[4][1],b[3][2],b[2][3],b[1][4],b[0][5]]
            ]

            xchar=["X","X","X","X","X","X"]
            ochar=["O","O","O","O","O","O"]
    except:
        return "Sorry, this only checks grids of 3x3 to 6x6."
    
    if xchar in bcheck:
        return "X"
    elif ochar in bcheck:
        return "O"
    else:
        return "NO WINNER"
    
tic_tac_toe(board1)

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    places=list(route_map.keys())
    times=list(route_map.values())

    s=0
    while s<len(route_map): #get first stop from keys
        if first_stop==places[s][0]: 
            start=s  #s=index of starting point
            break
        else:
            s+=1
   
    e=0
    while e<len(route_map): #get last stop from keys
        if second_stop==places[e][1]: 
            end=e #e=index of ending point
            break
        else:
            e+=1

    if end==start:
        travel=times[end]["travel_time_mins"]
    elif end>start:
        x=0
        travel=0
        while x<end-start+1:
            travel+=times[start+x]["travel_time_mins"]
            x+=1
    elif end<start:
        travel=0
        for x in range(start,len(route_map)):
            travel+=times[x]["travel_time_mins"]
        for x in range(0,end+1):
            travel+=times[x]["travel_time_mins"]
    
    return travel

eta("admu","upd",legs)
