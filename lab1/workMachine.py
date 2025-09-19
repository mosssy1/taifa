def milly_to_moore(milly):

    moore = {}
    
    for state in milly:
        for tup in milly[state]:
            curr = (tup[2], tup[1])
            if curr not in moore:
                moore[curr] = []
    
    for state in milly:  
        state_from_moore = -1
        
        for state1 in moore:  
            temp = state1[0]
            
            if (temp == state):
                state_from_moore = -1
                break
            else:
                state_from_moore = state
                
        if state_from_moore != -1:
            moore[(state_from_moore, '-')] = []

    for state in moore:
        for cort in milly[state[0]]:
            moore[state].append(cort)


    return moore

def moore_to_milly(moore):

    milly = []
    for i in range(1, len(moore)):
        for j in range(len(moore[i])):
            if moore[i][j] != '-':
                milly.append((j, i, moore[0][j], moore[i][j]))

    return milly
