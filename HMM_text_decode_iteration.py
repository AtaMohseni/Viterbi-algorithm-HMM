# -*- coding: utf-8 -*-
"""
Created on Mon May 22 14:35:54 2023

@author: ATA
"""

import numpy as np
import matplotlib.pyplot as plt
from Data_loader import Transition_matrix,Emission_matrix,Initial_state_distribution,sequence_observation

def Lit_star(transition,emission,initial_states,sequence_data):
    """ function to calculate log-prob of most likely t-step path of 
    hidden states that ends in S_t = i at time t and explain  observations
    O1,O2,..Ot"""
    
    """ transition - is a numpy array transition probability matrix of hidden 
    states with shape n x n or (27 x 27)
    emission - emission probability matrix with shape n x k or (27 x 2)
    initial_states - list length n, probability distribution of hidden states
    sequence_data - list of length T of 0 or 1 observations """
    
    Lit = np.zeros((len(transition),len(sequence_data)))

    for t,seq_observation in enumerate(sequence_data):
        
        if t == 0:
            Lit[:,t] = np.log(initial_states) + np.log(emission[:,int(seq_observation)])
        else:
            temp = []
            
            for states_j in range(len(initial_states)):
                temp = list(Lit[:, t-1] +  np.log(transition[:,states_j]))
                Lit[states_j,t] = max(temp) + np.log(emission[states_j,int(sequence_data[t])])
            
        if t % 10000 == 0:
            print('Time step','  ',t) 
    return Lit

def back_tracking(transition,emission,initial_states,sequence_data):
    """ function that records most likely states for all time steps,
    starting at time T, and ending at time 0. """
    
    Lit = Lit_star(transition,emission,initial_states,sequence_data)
    most_likely_states_reversed = []
    
    for t in range(len(sequence_data)):
        
        if t == 0:
            most_likely_states_reversed.append(np.where(Lit[:,t-1] == np.max(Lit[:,t-1]))[0][0])
        else:
            temp = list(Lit[:,-t-1] +  np.log(transition[:,int(most_likely_states_reversed[t-1])]))
            most_likely_states_reversed.append(np.where(temp == np.max(temp))[0][0])
            
    return most_likely_states_reversed

def decode(transition,emission,initial_states,sequence_data,possible_states):
    """ function that decode most likely hidden states (ignoring repeated elements)
    and return decoded sentence"""
    
    """ possible states - list of hidden states represent letters {a,b,...,z,space}
    of length n = 27"""
    
    most_likely_states_reversed = back_tracking(transition,emission,initial_states,sequence_data)
    
    decoded_letters_reversed = []
    
    for index,state in enumerate(most_likely_states_reversed):
        
        if index == 0:
            decoded_letters_reversed.append(possible_states[int(state)])
        else:
            if most_likely_states_reversed[index] != most_likely_states_reversed[index - 1]:
                decoded_letters_reversed.append(possible_states[int(state)])
    
    return ''.join(reversed(decoded_letters_reversed))
        
        
if __name__ == "__main__":

    tr = np.array(Transition_matrix())
    em = np.array(Emission_matrix())
    isd = Initial_state_distribution()
    seq =sequence_observation()
    possible_states = [chr(x) for x in range(97,123)] + [chr(32)]
    sentence  = decode(tr,em,isd,seq,possible_states)   
    print('\n')
    print('decoded sentence:')
    print(sentence)     
    
 