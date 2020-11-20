import numpy as np
from wolf_agent import WoLFAgent

from matrix_game_local_only import MatrixGame_local
from matrix_game_mec_only import MatrixGame_mec
from matrix_game import MatrixGame
from queue_relay import QueueRelay
import matplotlib.pyplot as plt

class draw_picture():

    def __init__(self):
        self.bandwidth = []
        self.usersnumber = []

    def run_for_all_mode(self,bw,un):
        nb_episode = 2000
        actions = np.arange(8)
        user_num = un
        lambda_n = np.zeros(user_num)
        for i in range(user_num):  # 每比特需要周期量 70~800 cycles/bits
            if i % 5 == 0:
                lambda_n[i] = 0.001
            if i % 5 == 1:
                lambda_n[i] = 0.01
            if i % 5 == 2:
                lambda_n[i] = 0.1
            if i % 5 == 3:
                lambda_n[i] = 0.001
            if i % 5 == 4:
                lambda_n[i] = 0.01
        actions_set = [[0, 5 * pow(10, 6), 0.4],
                       [0, 5 * pow(10, 6), 0.4],
                       [0, 5 * pow(10, 6), 0.4],
                       [0, 5 * pow(10, 6), 0.4],
                       [1, 0, 0.4],
                       [1, 0, 0.4],
                       [1, 0, 0.4],
                       [1, 0, 0.4]]
        GPD1_array = [4 * pow(10, 6) for _ in range(user_num)]
        GPD2_array = [0.3 for _ in range(user_num)]

        # init wolf agent
        wolf_agent_array = []
        for i in range(user_num):
            wolf_agent_array.append(WoLFAgent(alpha=0.1, actions=actions, high_delta=0.004, low_delta=0.002))

        queue_relay_array = []

        for i in range(user_num):
            queue_relay_array.append(QueueRelay(lambda_n[i], GPD1_array[i], GPD2_array[i]))

        # set reward functio

        # reward = Reward()
        reward_history = []
        # init_Queue_relay

        for episode in range(nb_episode):

            Q_array = []
            Qx_array = []
            Qy_array = []
            Qz_array = []
            M1_array = []
            M2_array = []

            for i in range(user_num):
                Q_array.append(queue_relay_array[i].Q)
                Qx_array.append(queue_relay_array[i].Qx)
                Qy_array.append(queue_relay_array[i].Qy)
                Qz_array.append(queue_relay_array[i].Qz)
                M1_array.append(queue_relay_array[i].M1)
                M2_array.append(queue_relay_array[i].M2)

            iteration_actions = []
            for i in range(user_num):
                iteration_actions.append(wolf_agent_array[i].act())
            game = MatrixGame(actions=iteration_actions, Q=Q_array,
                              Qx=Qx_array, Qy=Qy_array, Qz=Qz_array,
                              M1=M1_array,
                              M2=M2_array , BW= bw)

            reward, bn, lumbda, rff = game.step(actions=iteration_actions)
            for i in range(user_num):
                # wolf agent act
                # update_Queue_relay
                queue_relay_array[i].lumbda = lumbda[i]
                queue_relay_array[i].updateQ(bn[i], actions_set[iteration_actions[i]][0], rff[i])
                queue_relay_array[i].updateQx()
                queue_relay_array[i].updateQy()
                queue_relay_array[i].updateQz()

            # reward step
            reward_history.append(sum(reward))
            for i in range(user_num):
                wolf_agent_array[i].observe(reward=reward[i])

        # for i in range(user_num):
        #     print(wolf_agent_array[i].pi_average)

        # plt.plot(np.arange(len(reward_history)), reward_history, label="")
        # plt.show()

        return reward_history[-1]

    def run_for_only_mec(self,bw1,un1):
        nb_episode = 2000
        actions_set = [
            [1, 0, 0.1],
            [1, 0, 0.5],
            [1, 0, 1],
            [1, 0, 2]]
        actions = np.arange(len(actions_set))
        user_num = un1
        lambda_n = np.zeros(user_num)
        for i in range(user_num):  # 每比特需要周期量 70~800 cycles/bits
            if i % 5 == 0:
                lambda_n[i] = 0.001
            if i % 5 == 1:
                lambda_n[i] = 0.01
            if i % 5 == 2:
                lambda_n[i] = 0.1
            if i % 5 == 3:
                lambda_n[i] = 0.001
            if i % 5 == 4:
                lambda_n[i] = 0.01

        GPD1_array = [4 * pow(10, 6) for _ in range(user_num)]
        GPD2_array = [0.3 for _ in range(user_num)]

        # init wolf agent
        wolf_agent_array = []
        for i in range(user_num):
            wolf_agent_array.append(WoLFAgent(alpha=0.1, actions=actions, high_delta=0.004, low_delta=0.002))

        queue_relay_array = []

        for i in range(user_num):
            queue_relay_array.append(QueueRelay(lambda_n[i], GPD1_array[i], GPD2_array[i]))

        # set reward functio

        # reward = Reward()
        reward_history = []
        # init_Queue_relay

        for episode in range(nb_episode):

            Q_array = []
            Qx_array = []
            Qy_array = []
            Qz_array = []
            M1_array = []
            M2_array = []

            for i in range(user_num):
                Q_array.append(queue_relay_array[i].Q)
                Qx_array.append(queue_relay_array[i].Qx)
                Qy_array.append(queue_relay_array[i].Qy)
                Qz_array.append(queue_relay_array[i].Qz)
                M1_array.append(queue_relay_array[i].M1)
                M2_array.append(queue_relay_array[i].M2)

            iteration_actions = []
            for i in range(user_num):
                iteration_actions.append(wolf_agent_array[i].act())
            game = MatrixGame_mec(actions=iteration_actions, Q=Q_array,
                                  Qx=Qx_array, Qy=Qy_array, Qz=Qz_array,
                                  M1=M1_array,
                                  M2=M2_array, BW=bw1)

            #print('Q value :' + str(Q_array) + str(Qx_array) + str(Qy_array) + str(Qz_array))

            reward, bn, lumbda, rff = game.step(actions=iteration_actions)
            for i in range(user_num):
                # wolf agent act
                # update_Queue_relay
                queue_relay_array[i].lumbda = lumbda[i]
                queue_relay_array[i].updateQ(bn[i], actions_set[iteration_actions[i]][0], rff[i])
                queue_relay_array[i].updateQx()
                queue_relay_array[i].updateQy()
                queue_relay_array[i].updateQz()

            # reward step
            reward_history.append(sum(reward))
            for i in range(user_num):
                wolf_agent_array[i].observe(reward=reward[i])

        # for i in range(user_num):
        #     print(wolf_agent_array[i].pi_average)
        # plt.plot(np.arange(len(reward_history)), reward_history, label="")
        # plt.show()

        return reward_history[-1]

    def run_for_only_local(self,bw2,un2):
        nb_episode = 2000
        actions_set = [
            [0, 5 * pow(10, 6), 0],
            [0, 10 * pow(10, 6), 0],
            [0, 20 * pow(10, 6), 0],
            [0, 30 * pow(10, 6), 0]]
        actions = np.arange(len(actions_set))
        user_num = un2
        lambda_n = np.zeros(user_num)
        for i in range(user_num):  # 每比特需要周期量 70~800 cycles/bits
            if i % 5 == 0:
                lambda_n[i] = 0.001
            if i % 5 == 1:
                lambda_n[i] = 0.01
            if i % 5 == 2:
                lambda_n[i] = 0.1
            if i % 5 == 3:
                lambda_n[i] = 0.001
            if i % 5 == 4:
                lambda_n[i] = 0.01

        GPD1_array = [4 * pow(10, 6) for _ in range(user_num)]
        GPD2_array = [0.3 for _ in range(user_num)]

        # init wolf agent
        wolf_agent_array = []
        for i in range(user_num):
            wolf_agent_array.append(WoLFAgent(alpha=0.1, actions=actions, high_delta=0.004, low_delta=0.002))

        queue_relay_array = []

        for i in range(user_num):
            queue_relay_array.append(QueueRelay(lambda_n[i], GPD1_array[i], GPD2_array[i]))

        # set reward functio

        # reward = Reward()
        reward_history = []
        # init_Queue_relay

        for episode in range(nb_episode):

            Q_array = []
            Qx_array = []
            Qy_array = []
            Qz_array = []
            M1_array = []
            M2_array = []

            for i in range(user_num):
                Q_array.append(queue_relay_array[i].Q)
                Qx_array.append(queue_relay_array[i].Qx)
                Qy_array.append(queue_relay_array[i].Qy)
                Qz_array.append(queue_relay_array[i].Qz)
                M1_array.append(queue_relay_array[i].M1)
                M2_array.append(queue_relay_array[i].M2)

            iteration_actions = []
            for i in range(user_num):
                iteration_actions.append(wolf_agent_array[i].act())
            game = MatrixGame_local(actions=iteration_actions, Q=Q_array,
                                    Qx=Qx_array, Qy=Qy_array, Qz=Qz_array,
                                    M1=M1_array,
                                    M2=M2_array, BW=bw2)

            reward, bn, lumbda, rff = game.step(actions=iteration_actions)
            for i in range(user_num):
                # wolf agent act
                # update_Queue_relay
                queue_relay_array[i].lumbda = lumbda[i]
                queue_relay_array[i].updateQ(bn[i], actions_set[iteration_actions[i]][0], rff[i])
                queue_relay_array[i].updateQx()
                queue_relay_array[i].updateQy()
                queue_relay_array[i].updateQz()

            # reward step
            reward_history.append(sum(reward))
            for i in range(user_num):
                wolf_agent_array[i].observe(reward=reward[i])

        # for i in range(user_num):
        #     print(wolf_agent_array[i].pi_average)
        # plt.plot(np.arange(len(reward_history)), reward_history, label="")
        # plt.show()

        return reward_history[-1]


if __name__ == '__main__':
    #bandwidth = np.array([2*pow(10,6),4*pow(10,6),6*pow(10,6),8*pow(10,6),10*pow(10,6),12*pow(10,6),14*pow(10,6),16*pow(10,6)])
    usernumber = np.array([10,15,20,25,30,35,40,45])

    draw = draw_picture()

    cost_of_all = []
    cost_of_mec = []
    cost_of_local = []

    for i in range(8):
        cost_of_all.append(draw.run_for_all_mode(bw=10*pow(10,6), un=usernumber[i]))
        cost_of_mec.append(draw.run_for_only_mec(bw1=10*pow(10,6), un1=usernumber[i]))
        cost_of_local.append(draw.run_for_only_local(bw2=10*pow(10,6), un2=usernumber[i]))

    plt.plot(usernumber, cost_of_all, '^-', linewidth=0.4, label='all selection')
    plt.plot(usernumber, cost_of_local, '<-', linewidth=0.4, label='only local selection')
    plt.plot(usernumber, cost_of_mec, '>-', linewidth=0.4, label='only MEC selection')
    plt.grid(True)      #显示网格

    plt.xlabel('The number of UE')
    plt.ylabel('Sum Cost')
    plt.legend(loc='upper left')    #图例右上角
    plt.show()
    #plt.savefig('f1-num_ue.png')


