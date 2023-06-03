# Viterbi-algorithm-HMM
Implementation of Viterbi Algorithm to decode an English sentence from a long sequence of non-text observations. here n = 27 hidden states, S_t ∈ {1,2,..,27} and binary observation O_t ∈ {0,1}. Initial state distribution, transition matrix and emission matrix are already provided, so no learning is needed.
Time complexity of algorithm is O(n^2 T) where n is possible values of hidden states, and T is the total length of sequence to be decoded. 
