class QueueRelay:
    def __init__(self, lumbda, GPD1, GPD2):
        self.Q  = 0
        self.Qx = 0
        self.Qy = 0
        self.Qz = 0
        self.GPD1 = GPD1
        self.GPD2 = GPD2
        self.tau = pow(10,-3)         # time slot τ，1ms
        self.kmob = pow(10,-27)       #本地cpu核有效电容参数
        self.Li = 737.5             #737.5                      #mecCPU处理密度 单位 cycles/bits
        self.q0 = 3.96*pow(10,7)   #队列阈值设定,单位 bits ,参考dymatic文章
        self.lumbda = lumbda 
        self.F = 10 * pow(10,9)       # F =10Ghz     MEC 计算能力
        self.M1 = self.q0 + self.GPD1 / (1 - self.GPD2)
        self.M2 = 2 * self.GPD1 * self.GPD1 / ((1 - self.GPD2) * (1 - 2 * self.GPD2))

    def updateQ(self, bn, theta, rf):
        self.Q = max((self.Q + bn * theta - self.tau * rf / self.Li),0)

    def updateQx(self):
        self.Qx = max((self.Qx + self.Q - self.q0 * self.lumbda), 0)

    def updateQy(self):
        self.Qy = max((self.Qy + (self.Q - self.GPD1)*( 1 if self.Q > self.q0 else 0)), 0)

    def updateQz(self):
        self.Qz = max((self.Qz + ((self.Q - self.q0)*(self.Q - self.q0) - self.GPD2)*(1 if self.Q > self.q0 else 0)), 0)

    def updateM1(self):
        self.M1 = self.q0 + self.GPD1 / (1 - self.GPD2)

    def updateM2(self):
        self.M2 = 2 * self.GPD1 * self.GPD1 / ((1 - self.GPD2) * (1 - 2 * self.GPD2))



