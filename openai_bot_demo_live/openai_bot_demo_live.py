"""
DOCSTRING
"""
import gym
import random
import universe

def determine_turn(turn, observation_n, j, total_sum, prev_total_sum, reward_n):
    """
    reinforcement learning step

    for every 15 iterations, sum the total observations,
    and take the average if lower than 0, change the direction
    if we go 15+ iterations and get a reward each step,
    we're doing something right thats when we turn
    """
    if(j >= 15):
        if(total_sum/ j ) == 0:
            turn = True
        else:
            turn = False
        total_sum = 0
        j = 0
        prev_total_sum = total_sum
        total_sum = 0
    else:
        turn = False
    if(observation_n != None):
        j += 1
        total_sum += reward_n
    return(turn, j, total_sum, prev_total_sum)

def main():
    env = gym.make('flashgames.CoasterRacer-v0')
    observation_n = env.reset()
    n, j = 0, 0
    total_sum = 0
    prev_total_sum = 0
    turn = False
    left = [
        ('KeyEvent', 'ArrowUp', True),
        ('KeyEvent', 'ArrowLeft', True),
        ('KeyEvent', 'ArrowRight', False)]
    right = [
        ('KeyEvent', 'ArrowUp', True),
        ('KeyEvent', 'ArrowLeft', False),
        ('KeyEvent', 'ArrowRight', True)]
    Forward = [
        ('KeyEvent', 'ArrowUp', True),
        ('KeyEvent', 'ArrowLeft', False),
        ('KeyEvent', 'ArrowRight', False)]
    while True:
        n+=1
        if(n > 1):
            if(observation_n[0] != None):
                prev_score = reward_n[0]
                if(turn):
                    event = random.choice([left, right])
                    action_n = [event for ob in observation_n]
                    turn = False
        elif(~turn):
            action_n = [Forward for ob in observation_n]
        if(observation_n[0] != None):
            turn, j, total_sum, prev_total_sum = determine_turn(
                turn, observation_n[0], j, total_sum, prev_total_sum, reward_n[0])
        observation_n, reward_n, done_n, info = env.step(action_n)
        env.render()

if __name__ == '__main__':
    main()
