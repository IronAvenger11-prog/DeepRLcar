def progress_based_reward(params):
    # Extract relevant input parameters
    progress = params['progress']
    steps = params['steps']

    # Constants for reward calculation
    BASE_REWARD = 1e-5
    MAX_REWARD = 5.0

    # Calculate reward based on progress
    progress_reward = progress / steps
    reward = BASE_REWARD + MAX_REWARD * progress_reward

    # Cap the maximum reward
    reward = min(reward, MAX_REWARD)

    # Always return a float value
    return float(reward)
