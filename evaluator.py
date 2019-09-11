import random

import turingarena as ta


def evaluate_testcase(input_necklace_colors):
    #print(f"Testing with n = {len(input_necklace)} necklace = {input_necklace} ...", end=" ")
    print(f"Testing with a necklace of {len(input_necklace)} beads ...", end=" ")
    def num_breakpoints(necklace_colors):
        risp = 0
        if necklace_colors[len(necklace_colors)-1] != necklace_colors[0]:
            risp += 1
        for pos in range(len(necklace_colors)-1):
            if necklace_colors[pos] != necklace_colors[pos+1]:
                risp += 1
        return risp
    
    n = len(input_necklace_colors)
    current_necklace_colors = input_necklace_colors[:]
    current_necklace_names = list(range(1,n+1))
    pos_of_bead = [None]+list(range(n))    

    def reverse_integral(a_name,b_name):
        #print(f"Evaluator reverse_integral(a_name={a_name},b_name={b_name})")

        nonlocal current_necklace_colors, current_necklace_names, pos_of_bead
        def swap(a_pos,b_pos):
            #print(f"Evaluator swap(a_pos={a_pos},b_pos={b_pos})")
            nonlocal current_necklace_colors, current_necklace_names, pos_of_bead
            pos_of_bead[current_necklace_names[b_pos]] = a_pos
            pos_of_bead[current_necklace_names[a_pos]] = b_pos
            tmp = current_necklace_names[a_pos]
            current_necklace_names[a_pos] = current_necklace_names[b_pos]
            current_necklace_names[b_pos] = tmp
            tmp = current_necklace_colors[a_pos]
            current_necklace_colors[a_pos] = current_necklace_colors[b_pos]
            current_necklace_colors[b_pos] = tmp
            
        a_pos = pos_of_bead[a_name]
        b_pos = pos_of_bead[b_name]
        finished = False
        while not finished: 
            swap(a_pos,b_pos)
            a_pos = (a_pos + 1) % n
            if a_pos == b_pos:
                finished = True
            b_pos = (b_pos - 1 +n) % n
            if a_pos == b_pos:
                finished = True
                
    try:
        def reverse_interval(a_name, b_name):
            nonlocal num_made_moves, n
            #print(f"reverse_interval(a = {a_name}, b={b_name}) called.")
            if a_name < 0 or a_name > n or b_name < 0 or b_name > n:
                print(f"WRONG: The call reverse_interval(a = {a_name}, b={b_name}) is not valid.")
                ta.goals.setdefault("solve_in_any_number_of_moves", False)
                ta.goals.setdefault("at_most_n2_moves", False)
                ta.goals.setdefault("opt_solve", False)
                ta.goals.setdefault("linear_time", False)
            else:
                num_made_moves += 1
                reverse_integral(a_name,b_name)

        #expected_answer = (num_breakpoints(input_necklace_colors)-2)/2
        with ta.run_algorithm("solutions/only_num_moves_correct.c") as p:
            expected_answer = p.functions.necklace(len(input_necklace), input_necklace, callbacks=[reverse_interval])

        # print(f"The reference solution says that the minimum number of moves is {expected_answer}")
        
        num_made_moves = 0
        with ta.run_algorithm(ta.submission.source) as p:
            obtained_answer = p.functions.necklace(len(input_necklace), input_necklace, callbacks=[reverse_interval])
    except ta.AlgorithmError as e:
        print(f" error: {e}")
        ta.goals.setdefault("correct_num_moves", False)
        ta.goals.setdefault("solve_in_any_number_of_moves", False)
        ta.goals.setdefault("at_most_n2_moves", False)
        ta.goals.setdefault("opt_solve", False)
        ta.goals.setdefault("linear_time", False)
        
    print(f"(time: {int(p.time_usage * 1000000)} us)")

    if obtained_answer == expected_answer:
        print(f" Correct minimum number of moves!", end=" ")
    else:
        ta.goals.setdefault("correct_num_moves", False)
        print(f"We disagree on the minimum number of moves needed to solve the necklace {input_necklace}. Your answer is {obtained_answer} while we believe the correct number is {expected_answer}.", end=" ")

    if num_breakpoints(current_necklace_colors) > 2:
        ta.goals.setdefault("solve_in_any_number_of_moves", False)
        ta.goals.setdefault("at_most_n2_moves", False)
        ta.goals.setdefault("opt_solve", False)
        ta.goals.setdefault("linear_time", False)
        if num_made_moves == 0:
            print(f" Your solution did no move.")
        else:
            print(f"Starting from the necklace {input_necklace_colors} your solution ends up with the necklace {current_necklace_colors} which is NOT entirely solved!", end=" ")
    else:
        if expected_answer > 0:
            print(f"Correct: your procedure fully solved the necklace.")
        else:
            print(f"Correct: no move was needed and no move was done by your code.")

    if num_made_moves > n*n:
        print(f"But used quite a lot of moves.")
        ta.goals.setdefault("at_most_n2_moves", False)
        ta.goals.setdefault("linear_time", False)

    if int(p.time_usage * 1000000) > 2000:
        print(f"Your procedure is too slow. There exists a linear time solution to this problem.")
        ta.goals.setdefault("linear_time", False)


for n in [6,10,20,50,100,200]:
    for _ in range(3):
        input_necklace = [ random.choice([0,1]) for _ in range(n) ]
        evaluate_testcase(input_necklace)

ta.goals.setdefault("correct_num_moves", True)
ta.goals.setdefault("solve_in_any_number_of_moves", True)
ta.goals.setdefault("at_most_n2_moves", True)
ta.goals.setdefault("opt_solve", True)
ta.goals.setdefault("linear_time", True)
print(ta.goals)
