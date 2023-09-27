def advanced_reward_function(params):
    # Extract relevant input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    progress = params['progress']
    steps = params['steps']

    # Constants for reward calculation
    BASE_REWARD = 1e-5
    MAX_REWARD = 5.0
    MIN_DISTANCE_FROM_CENTER = 0.02
    MAX_STEPS = 1000  # You can adjust this based on the race duration

    # Calculate reward based on conditions
    if all_wheels_on_track:
        # Calculate a reward multiplier based on the distance from the center
        distance_reward = 1.0 - (distance_from_center / (0.5 * track_width))

        # Ensure the agent gets higher rewards for staying close to the center
        if distance_reward < 0:
            distance_reward = 0

        # Calculate a progress-based reward to encourage forward movement
        progress_reward = progress / MAX_STEPS

        # Combine distance and progress rewards
        reward = BASE_REWARD + MAX_REWARD * (distance_reward + progress_reward)

        # Cap the maximum reward to avoid excessive rewards
        reward = min(reward, MAX_REWARD)

    else:
        # If the agent goes off track, give a minimal reward
        reward = BASE_REWARD

    # Always return a float value
    return float(reward)
