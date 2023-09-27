def combined_reward(params):
    # Extract relevant input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    progress = params['progress']
    steps = params['steps']

    # Constants for reward calculation
    BASE_REWARD = 1e-5
    MAX_REWARD = 5.0
    MIN_DISTANCE_FROM_CENTER = 0.02

    # Calculate reward based on distance from the center and progress
    distance_reward = 1.0 - (distance_from_center / (0.5 * track_width))
    progress_reward = progress / steps

    # Combine distance and progress rewards
    reward = BASE_REWARD + MAX_REWARD * (distance_reward + progress_reward)

    # Cap the maximum reward
    reward = min(reward, MAX_REWARD)

    # Always return a float value
    return float(reward)
