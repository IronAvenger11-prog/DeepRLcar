def proximity_based_reward(params):
    # Extract relevant input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']

    # Constants for reward calculation
    BASE_REWARD = 1e-5
    MAX_REWARD = 5.0
    MIN_DISTANCE_FROM_CENTER = 0.02

    # Calculate reward based on distance from the center
    if distance_from_center <= 0.5 * track_width:
        reward = MAX_REWARD
    else:
        reward = BASE_REWARD

    # Always return a float value
    return float(reward)
