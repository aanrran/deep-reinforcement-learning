import numpy as np
from collections import defaultdict

class Agent:

    def __init__(self, nA=6):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        
        self.epsilon = 1.0
        self.alpha = 0.3
        self.gamma = 0.9
        
        self.state = 0
        self.action = 0
        
        self.eps = 0.005
        self.i_episode = 0
        
        self.q_learning = True
        
    def epsilon_greedy_probs(self, state):
        """ obtains the action probabilities corresponding to epsilon-greedy policy """

        if self.q_learning == True:
            self.epsilon = max(1.0/self.i_episode, self.eps)
        else:
            self.epsilon = self.eps
            
        policy_s = np.ones(self.nA) * self.epsilon / self.nA
        policy_s[np.argmax(state)] = 1 - self.epsilon + (self.epsilon / self.nA)
        return policy_s

    def select_action(self, state, i_episode):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        self.i_episode = i_episode
        policy = self.epsilon_greedy_probs(self.Q[state])
        self.action = np.random.choice(np.arange(self.nA), p=policy) if state in self.Q else np.random.choice(self.nA)
        self.state = state
        return self.action

    def step(self, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        Qsa = self.Q[self.state][self.action]
        Qs_next = self.Q[next_state]
        if self.q_learning == True:
            self.Q[self.state][self.action] = Qsa + (self.alpha * (reward + (self.gamma * np.max(Qs_next)) - Qsa)) 
        else:
            policy = self.epsilon_greedy_probs(self.Q[next_state])
            self.Q[self.state][self.action] = Qsa + (self.alpha * (reward + (self.gamma * np.dot(policy, Qs_next)) - Qsa))
        