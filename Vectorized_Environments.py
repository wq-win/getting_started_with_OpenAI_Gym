# get the neccasary stuff 
import gym
from baselines.common.vec_env.subproc_vec_env import SubprocVecEnv # type: ignore


if __name__=='__main__':
    # list of envs 
    num_envs = 3
    envs = [lambda: gym.make("BreakoutNoFrameskip-v4") for i in range(num_envs)]

    # Vec Env 
    envs = SubprocVecEnv(envs)

    # Get initial state
    init_obs = envs.reset()


    # We get a list of observations corresponding to parallel environments 
    print("Number of Envs:", len(init_obs))

    # Check out of the obs 
    one_obs = init_obs[0]
    print("Shape of one Env:", one_obs.shape)

    # prepare a list of actions and apply them to environment 
    actions = [0, 1, 2]
    obs = envs.step(actions)

    # render the envs
    import time 

    # list of envs 
    num_envs = 3
    envs = [lambda: gym.make("BreakoutNoFrameskip-v4") for i in range(num_envs)]

    # Vec Env 
    envs = SubprocVecEnv(envs)

    init_obs = envs.reset()

    for i in range(1000):
        actions = [envs.action_space.sample() for i in range(num_envs)]
        envs.step(actions)
        envs.render()
        time.sleep(0.001)

    envs.close()