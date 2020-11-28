import numpy as np
from wolf_agent import WoLFAgent

from matrix_game_local_only import MatrixGame_local
# from matrix_game_mec_only import MatrixGame_mec
from matrix_game import MatrixGame
from queue_relay import QueueRelay
import matplotlib.pyplot as plt

from gpd import GPD     ##  TLIU
from dataToExcel import DTE    ##  TLIU
import xlrd      ##  TLIU
import xlsxwriter    ##  TLIU

'''
    这个draw.py记录了cost_local
'''

class draw_picture():

    def __init__(self):
        self.bandwidth = []
        self.usersnumber = []
        self.gpdaa = GPD()

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

        cost_local_history = []
        # init_Queue_relay

        Q_array_histroy = [[10] for i in range(user_num)]  ##  TLIU

        for episode in range(nb_episode):
            print('episode for all :',episode)

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

            for i in range(user_num):
                Q_array_histroy[i].append(Q_array[i])
            if episode % 50 == 0 and episode != 0:
                for i in range(user_num):

                    data = Q_array_histroy[i]
                    # data = [10000000000000 for i in range(200) ]
                    # res = aa.gpd(  data  , 3.96*pow(10,5)  )
                    res = self.gpdaa.gpd(data, 3.96 * pow(10, 7))
                    if res:
                        queue_relay_array[i].GPD1 = res[0][0]
                        queue_relay_array[i].GPD2 = res[0][1]
                        queue_relay_array[i].updateM1()
                        queue_relay_array[i].updateM2()

            iteration_actions = []
            for i in range(user_num):
                iteration_actions.append(wolf_agent_array[i].act())
            game = MatrixGame(actions=iteration_actions, Q=Q_array,
                              Qx=Qx_array, Qy=Qy_array, Qz=Qz_array,
                              M1=M1_array,
                              M2=M2_array , BW= bw)

            reward, cost_local, bn, lumbda, rff = game.step(actions=iteration_actions)
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

            cost_local_history.append(sum(cost_local))

            for i in range(user_num):
                wolf_agent_array[i].observe(reward=reward[i])

        # for i in range(user_num):
        #     print(wolf_agent_array[i].pi_average)

        plt.plot(np.arange(len(reward_history)), reward_history, label="")
        plt.title('all mode ')
        plt.show()
        print('reward_history[-1]:',reward_history[-1])

        return cost_local_history[-1]


    def run_for_only_local(self,bw2,un2):
        nb_episode =2000
        # gpdaa = GPD()
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

        cost_local_history = []

        # init_Queue_relay


        Q_array_histroy = [[10] for i in range(user_num)]  ##  TLIU

        for episode in range(nb_episode):
            print('episode for local ',episode)

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

            for i in range(user_num):
                Q_array_histroy[i].append(Q_array[i])
            if episode % 50 == 0 and episode != 0:
                for i in range(user_num):
                    aa = GPD()
                    data = Q_array_histroy[i]
                    # data = [10000000000000 for i in range(200) ]
                    # res = aa.gpd(  data  , 3.96*pow(10,5)  )
                    res = self.gpdaa.gpd(data, 3.96 * pow(10, 7))
                    if res:
                        queue_relay_array[i].GPD1 = res[0][0]
                        queue_relay_array[i].GPD2 = res[0][1]
                        queue_relay_array[i].updateM1()
                        queue_relay_array[i].updateM2()


            iteration_actions = []
            for i in range(user_num):
                iteration_actions.append(wolf_agent_array[i].act())
            game = MatrixGame_local(actions=iteration_actions, Q=Q_array,
                                    Qx=Qx_array, Qy=Qy_array, Qz=Qz_array,
                                    M1=M1_array,
                                    M2=M2_array, BW=bw2)

            reward, cost_local, bn, lumbda, rff = game.step(actions=iteration_actions)
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
            cost_local_history.append(sum(cost_local))


            for i in range(user_num):
                wolf_agent_array[i].observe(reward=reward[i])

        plt.plot(np.arange(len(reward_history)), reward_history, label="")
        plt.title('only local mode ')
        plt.show()
        print('reward_history[-1]:',reward_history[-1])

        return cost_local_history[-1]


if __name__ == '__main__':
    bandwidth = np.array([2*pow(10,6),4*pow(10,6),6*pow(10,6),8*pow(10,6),10*pow(10,6),12*pow(10,6),14*pow(10,6)])
    #usernumber = np.array([10,15,20,25,30,35,40,45])

    draw = draw_picture()

    cost_of_all_10ge = []
    # cost_of_mec = []
    cost_of_local_10ge = []
    cost_of_all_15ge = []
    cost_of_all_20ge = []
    cost_of_all_25ge = []


    for i in range(7):
        cost_of_all_10ge.append(draw.run_for_all_mode(bw=bandwidth[i], un=10))
        # cost_of_mec.append(draw.run_for_only_mec(bw1=bandwidth[i], un1=10))
        cost_of_local_10ge.append(draw.run_for_only_local(bw2=bandwidth[i], un2=10))
        cost_of_all_15ge.append(draw.run_for_all_mode(bw=bandwidth[i], un=15))
        cost_of_all_20ge.append(draw.run_for_all_mode(bw=bandwidth[i], un=20))
        cost_of_all_25ge.append(draw.run_for_all_mode(bw=bandwidth[i], un=25))

    plt.plot(bandwidth, cost_of_all_10ge, '^-', linewidth=0.4, label='all selection')
    plt.plot(bandwidth, cost_of_local_10ge, '<-', linewidth=0.4, label='only local selection')
    # plt.plot(bandwidth, cost_of_mec, '>-', linewidth=0.4, label='only MEC selection')
    plt.plot(bandwidth, cost_of_all_15ge, '<-', linewidth=0.2, label='all selection of 15 UEs')
    plt.plot(bandwidth, cost_of_all_20ge, '<-', linewidth=0.2, label='all selection of 20 UEs')
    plt.plot(bandwidth, cost_of_all_25ge, '<-', linewidth=0.2, label='all selection of 25 UEs')

    plt.grid(True)      #显示网格

    plt.xlabel('The Bandwidth of Channel')
    plt.ylabel(' Cost_local')
    plt.legend(loc='upper right')    #图例右上角
    plt.show()

    # data = DTE("./picture/pic4/all_10ge")   ##  TLIU
    # print(cost_of_all_10ge)
    # data.write(cost_of_all_10ge)
    #
    # # data = DTE("./picture/pic4/mec")   ##  TLIU
    # # print(cost_of_mec)
    # # data.write(cost_of_mec)
    #
    # data = DTE("./picture/pic4/local_10ge")   ##  TLIU
    # print(cost_of_local_10ge)
    # data.write(cost_of_local_10ge)
    #
    # data = DTE("./picture/pic4/all_15_UEs")   ##  TLIU
    # print(cost_of_all_15ge)
    # data.write(cost_of_all_15ge)
    #
    # data = DTE("./picture/pic4/all_20_UEs")   ##  TLIU
    # print(cost_of_all_20ge)
    # data.write(cost_of_all_20ge)
    #
    # data = DTE("./picture/pic4/all_25_UEs")   ##  TLIU
    # print(cost_of_all_25ge)
    # data.write(cost_of_all_25ge)




