[//]: # "Image References"

[image1]: https://user-images.githubusercontent.com/10624937/42135619-d90f2f28-7d12-11e8-8823-82b970a54d7e.gif "Trained Agent"

# Project 1: Navigation

### Introduction

For this project, I trained an agent to navigate (and collect bananas) in a large, square world, using computer vision.  

![Trained Agent][image1]

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana.  Thus, the goal of your agent is to collect as many yellow bananas as possible while avoiding blue bananas.  

For the basic version, the state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around agent's forward direction.  Given this information, the agent has to learn how to best select actions.  Four discrete actions are available, corresponding to:
- **`0`** - move forward.
- **`1`** - move backward.
- **`2`** - turn left.
- **`3`** - turn right.

The task is episodic, and in order to solve the environment, the agent must get an average score of +13 over 100 consecutive episodes.

### Environment Setup:

1. Download the environment from one of the links below.  You need only select the environment that matches your operating system:
    - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)
    
    (_For Windows users_) Check out [this link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

    (_For AWS_) If you'd like to train the agent on AWS (and have not [enabled a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md)), then please use [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux_NoVis.zip) to obtain the environment.

2. Place the file in the DRLND GitHub repository, in the `p1_navigation/` folder, and unzip (or decompress) the file. 

### File Information:

- Navigation.ipynb: the whole code for the basic version of this project. The input state is a simple 37 elements array.
- Navigation_Pixels.ipynb: the challenge version of this project. The agent has to use computer vision to navigate.
- model.pth: this file is the trained basic agent model that contains the saved Model Weights for this project
- scores.csv: this file stores my basic agent performance scores during training

### Training Code and Framework:

Please look at Navigation.ipynb and Navigation_Pixels.ipynb for reference.

### Training Results:

My basic agent training take place in file `Navigation.ipynb`. The agent took about 535 episodes to reach 13 average score:

<img src="./Image/report.JPG" alt="image1"  width="800" height="500"/>.

### Challenge: Learning from Pixels

In the basic version, my agent learned from information such as its velocity, along with ray-based perception of objects around its forward direction. After I have successfully completed the project,  I created a new agent that learns directly from pixels. This advanced environment is almost identical to the basic environment, where the only difference is that the state is an 84 x 84 RGB image, corresponding to the agent's first-person view.

### Future Work:

- design more data efficient agent with PER(Prioritized Replay).
- fine tune the agent to get better score(now my Pixel version code runs well, but the average score still can not reach 13. I am still training, and hopefully it will be successful this time. The training time takes many hours.)