
####
# Each team's file must define four tokens:
#     team9
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'team9' # Only 10 chars displayed.
strategy_name = 'titfortat'
strategy_description = 'Replicate the enemies'
    
def titfortat(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    
    
    #tit for tat code but starts with betray, doesn't work yet
    
    if their_history is '':
        return 'b'
    if their_history is 'b':
        return 'b'
    else:
        return 'c'
    
    
    
    #test1 betray first move
   # if '' in my_history:
    #    return 'b'
    
    #test 2 betray no matter what
    #if their_history is 'b' or 'c':
     #   return 'b'
    # remove hashtag for test3 if 'b' in their_history:
     #   return 'b'
    #else:
     #   return 'c'
    
    #always collude
    #if their_history is 'b' or 'c':
       # return 'c'
    
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
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'First round betray passes'
     
     
      # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              
     # Test 2: Continue betraying if they collude despite being betrayed.
    if test_move(my_history='bbb',
              their_history='ccc', 
              my_score=0, 
              their_score=0,
              result='b'):
            print 'Infinite betray passes'
    
    
    #test 3: grudge(works)
    if test_move(my_history='c', their_history='b',
    my_score=-750,
    their_score=300,
    result='b'):
        print 'Grudge passes'
    #test 4: tit for tat
    if test_move(my_history='c', their_history='b',
    my_score=0, their_score=0, result='b'):
        print 'Tit for tat betray passes'
    #test 5: tit for tat collude
    if test_move(my_history='bbc', their_history='bcb', my_score=0, their_score=0, result='c'):
        print 'Tit for tat collude passes'
        
    #Test 6: grudge but should not retaliate since enemy uses collude
    if test_move(my_history='c', their_history='c', my_score=0, their_score=0, result='c'):
        print 'Grudge collude passes'
    #test 7: always collude
    if test_move(my_history='c', their_history='b', my_score=-500, their_score=150, result='c'):
        print 'Always collude passes'         