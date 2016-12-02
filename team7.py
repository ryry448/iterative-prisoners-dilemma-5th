####
# Each team's file must define four tokens:
#     team_name: Team 3
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team 3' # Only 10 chars displayed.
strategy_name = 'I love random'
strategy_description = 'Betray and collude randomly until score falls below -500, then always betray'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    #Betray and collude randomly until score falls below -500, then always betray
    if my_score > -500:
        import random
        random.seed()
        if random.choice([1,2]) == 1:
            return 'b'
        else:
            return 'c'
    else:
        return 'b'
    
    
    '''
    #betray every time
    return 'b'
    '''
    
    '''
    #Collude on the first move and then betray every move after
    if len(my_history) == 0:
        return 'c'
    else:
        return 'b'
    '''
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    #Random until -500
    test_move('', '', 500, 0, result='b')
    test_move('', '', -501, 0, result='b')
    
    #Always Betray
    test_move('', '', 0, 0, result='b')
    
    #Collude only the first time
    test_move('', '', 0, 0, result='c')
    test_move('cbc', 'bcb', 0, 0, result='b')
    