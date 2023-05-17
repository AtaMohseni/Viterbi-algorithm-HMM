# -*- coding: utf-8 -*-
"""
Created on Wed May 17 13:27:17 2023

@author: ATA
"""

def Transition_matrix():
    try:
        fhand = open("./transitionMatrix.txt")
    except:
        print ('the file does not exist')
        return None
    transition = []
    for line in fhand:
        transition.append(list(map(float,list (line.split()) )))
        
    return transition

def Emission_matrix():
    try:
        fhand = open("./emissionMatrix.txt")
    except:
        print ('the file does not exist')
        return None
    emission = []
    for line in fhand:
        emission.append(list(map(float,list (line.split()) )))
        
    return emission  

def Initial_state_distribution():
    try:
        fhand = open("./initialStateDistribution.txt")
    except:
        print ('the file does not exist')
        return None
    isd = []
    for line in fhand:
        isd.append(float(line.strip()))
        
    return isd    

def sequence_observation():
    try:
        fhand = open("./observations.txt")
    except:
        print ('the file does not exist')
        return None
    
    for line in fhand:
        obs = list(map(int,line.split() ))
        
    return obs
    