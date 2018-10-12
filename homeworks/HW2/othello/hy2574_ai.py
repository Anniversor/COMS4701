#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""
COMS W4701 Artificial Intelligence - Programming Homework 2

An AI player for Othello. This is the template file that you need to  
complete and submit. 

@author:  Haoyu Yan hy2574
"""

import random
import sys
import time

# You can use the functions in othello_shared to write your AI 
from othello_shared import find_lines, get_possible_moves, get_score, play_move

def compute_utility(board, color):
    anti_color = -color + 3
    count = 0
    anti_count = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == color:
                count += 1
            elif board[i][j] == anti_color:
                anti_count += 1
                
    return count - anti_count


############ MINIMAX ###############################

def minimax_min_node(board, color):
    anti_color = 3 - color
    moves = get_possible_moves(board, anti_color)
    if not moves:
        return compute_utility(board, color)
    mini_score = float("inf")

    for move in moves:
        new_board = play_move(board, anti_color, move[0], move[1])
        
        score = minimax_max_node(new_board, color)

        if score<mini_score:
            mini_score = score

    return mini_score


def minimax_max_node(board, color):

    moves = get_possible_moves(board, color)
    if not moves:
        return compute_utility(board, color)
    max_score = float("-inf")

    for move in moves:
        new_board = play_move(board, color, move[0], move[1])
        score = minimax_min_node(new_board, color)
        if score>max_score:
            max_score = score

    return max_score

    
def select_move_minimax(board, color):
    moves = get_possible_moves(board, color)
    max_score = float("-inf")
    best_move = [moves[0][0],moves[0][1]]
    for move in moves:
        new_board = play_move(board, color, move[0], move[1])
        score = minimax_min_node(new_board, color)
        if score>max_score:
            max_score = score
            best_move[0] = move[0]
            best_move[1] = move[1]

    return best_move[0], best_move[1]


############ ALPHA-BETA PRUNING #####################

states_cache = {}
limit = 7
#alphabeta_min_node(board, color, alpha, beta, level, limit)
def alphabeta_min_node(board, color, alpha, beta, level, limit): 
    anti_color = 3 - color
    moves = get_possible_moves(board, anti_color)
    if not moves:
        states_cache[board] = compute_utility(board, color) #update cache
        return compute_utility(board, color)
    mini_score = float("inf")
    boards = []

    for move in moves:
        boards.append(play_move(board, anti_color, move[0], move[1]))
    boards.sort(key=lambda x:compute_utility(x,color))

    for new_board in boards:
        # new_board = play_move(board, anti_color, move[0], move[1])
        if new_board in states_cache:
            score = states_cache[new_board]
        else:
            if level>=limit:
                score = compute_utility(new_board, color)
            else:
                score = alphabeta_max_node(new_board, color, alpha, beta,level+1,limit)
                states_cache[new_board] = score
        
        if score<mini_score:
            mini_score = score
        if mini_score<= alpha:
            return score
        beta = min(beta, mini_score)
    return mini_score


#alphabeta_max_node(board, color, alpha, beta, level, limit)
def alphabeta_max_node(board, color, alpha, beta, level, limit):

    moves = get_possible_moves(board, color)
    if not moves:
        states_cache[board] = compute_utility(board, color) #update cache
        return compute_utility(board, color)
    max_score = float("-inf")
    boards = []
    for move in moves:
        boards.append(play_move(board, color, move[0], move[1]))
    boards.sort(key=lambda x:compute_utility(x,color), reverse=True)

    for new_board in boards:       
        # new_board = play_move(board, color, move[0], move[1])
        if new_board in states_cache:
            score = states_cache[new_board]
        else:
            if  level>=limit:
                score = compute_utility(new_board, color)
            else:
                score = alphabeta_min_node(new_board, color, alpha, beta,level+1,limit)
                states_cache[new_board] = score

        if score>max_score:
            max_score = score
        if max_score>=beta:

            return max_score
        alpha = max(alpha, max_score)

    return max_score


def select_move_alphabeta(board, color): 
    moves = get_possible_moves(board, color)
    max_score = float("-inf")
    best_move = [0, 0]
    alpha = float("-inf")
    beta = float("inf")
    for move in moves:
        new_board = play_move(board, color, move[0], move[1])
        score = alphabeta_min_node(new_board, color, alpha, beta,1, limit)
        if score>max_score:
            max_score = score
            best_move[0] = move[0]
            best_move[1] = move[1]
        alpha = max(alpha, max_score)

    return best_move[0], best_move[1]


####################################################
def run_ai():
    """
    This function establishes communication with the game manager. 
    It first introduces itself and receives its color. 
    Then it repeatedly receives the current score and current board state
    until the game is over. 
    """
    print("Minimax AI") # First line is the name of this AI  
    color = int(input()) # Then we read the color: 1 for dark (goes first), 
                         # 2 for light. 

    while True: # This is the main loop 
        # Read in the current game status, for example:
        # "SCORE 2 2" or "FINAL 33 31" if the game is over.
        # The first number is the score for player 1 (dark), the second for player 2 (light)
        next_input = input() 
        status, dark_score_s, light_score_s = next_input.strip().split()
        dark_score = int(dark_score_s)
        light_score = int(light_score_s)

        if status == "FINAL": # Game is over. 
            print 
        else: 
            board = eval(input()) # Read in the input and turn it into a Python
                                  # object. The format is a list of rows. The 
                                  # squares in each row are represented by 
                                  # 0 : empty square
                                  # 1 : dark disk (player 1)
                                  # 2 : light disk (player 2)
                    
            # Select the move and send it to the manager 
            # movei, movej = select_move_minimax(board, color)
            movei, movej = select_move_alphabeta(board, color)
            print("{} {}".format(movei, movej)) 


if __name__ == "__main__":
    run_ai()
