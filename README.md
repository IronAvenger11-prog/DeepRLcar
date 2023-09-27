# Reinforcement Learning for Autonomous Racecar Navigation

Welcome to my autonomous racecar navigation project! 🏎️

## Project Overview

In this project, I embark on an exciting journey to train a cutting-edge autonomous racecar to master the art of navigating complex racetracks. The primary objective is to make our racecar autonomously follow the track's midline while staying within the track boundaries, all while maximizing rewards.

## Approach

### Leveraging State-of-the-Art Techniques

To accomplish this ambitious goal, I'm harnessing the power of state-of-the-art deep reinforcement learning techniques. In particular, I'm using **Proximal Policy Optimization (PPO)**, a reinforcement learning algorithm known for its effectiveness in training agents for complex tasks.

### Reward Maximization

The key to training a successful autonomous racecar lies in defining a rewarding experience. I've carefully crafted reward functions that encourage the racecar to exhibit the desired behavior:

1. **Proximity-Based Reward**: Rewarding the racecar for staying close to the track's center, promoting precise navigation.

2. **Progress-Based Reward**: Encouraging the racecar to make progress by rewarding it for advancing along the racetrack.

3. **Combined Reward**: Combining proximity and progress rewards to strike the perfect balance between precision and progress.

## Code Variations

In pursuit of the ultimate racing agent, I've explored multiple variations of the reward functions. Here's a glimpse of the code variants I've developed:

- [Proximity-Based Reward](code/proximity_based_reward.py): Rewarding the agent based on its proximity to the track center.
- [Progress-Based Reward](code/progress_based_reward.py): Rewarding the agent based on its progress along the track.
- [Combined Reward](code/combined_reward.py): Combining proximity and progress rewards for a comprehensive training experience.

## Getting Started

Want to take a spin with my code? Follow these simple steps:

1. Clone this repository.
2. Install the necessary dependencies (details in the README.md).
3. Run the autonomous racecar simulation with your chosen reward function.

## Demo
Watch this video to see a demonstration of the training with Amazon DeepRacer League : (https://youtu.be/Sbg7lwpT5Bk)
