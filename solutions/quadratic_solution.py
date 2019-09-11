def necklace(n, input_necklace_colors, reverse_interval):
    
    def num_breakpoints(necklace_colors):
        risp = 0
        if necklace_colors[len(necklace_colors)-1] != necklace_colors[0]:
            risp += 1
        for pos in range(len(necklace_colors)-1):
            if necklace_colors[pos] != necklace_colors[pos+1]:
                risp += 1
        return risp

    num_needed_moves = (num_breakpoints(input_necklace_colors)-2)/2

    current_necklace_colors = input_necklace_colors[:]
    current_necklace_names = list(range(1,n+1))
    pos_of_bead = [None]+list(range(n))
    
    def perform_move_in_local(a_name,b_name):
        nonlocal current_necklace_colors, current_necklace_names, pos_of_bead
        def swap(a_pos,b_pos):
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

    while num_breakpoints(current_necklace_colors) > 2:
        if current_necklace_colors[0] != current_necklace_colors[n-1]:
            pos1 = 0
        else:
            pos1 = 1
            while current_necklace_colors[pos1] == current_necklace_colors[pos1-1]:
                pos1 += 1
        pos2 = pos1 + 1
        while current_necklace_colors[pos2] == current_necklace_colors[pos2-1]:
            pos2 += 1
        pos3 = pos2 + 1
        while current_necklace_colors[pos3] == current_necklace_colors[pos3-1]:
            pos3 += 1
        reverse_interval(current_necklace_names[pos1],current_necklace_names[pos3-1])
        perform_move_in_local(current_necklace_names[pos1],current_necklace_names[pos3-1])

    return num_needed_moves
