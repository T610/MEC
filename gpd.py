import matlab
import matlab.engine
import numpy as np
# engine = matlab.engine.start_matlab() # Start MATLAB process
# engine = matlab.engine.start_matlab("-desktop") # Start MATLAB process with graphic UI

class GPD:
    def __init__(self):
        self.engine = matlab.engine.start_matlab() # Start MATLAB process
        print("start GPD")



    def gpd(self,data,threshold):

        # 取得是过去10的倍数的值  并且超过阈值
        segment = len(data) // 10
        data = data[ -1*segment*10: ]
        print(data)
        temp = []
        left = -1*segment*10
        for i in range(segment) :
            right = left + 10
            if right == 0:
                mid = data[left:]
            else:
                mid = data[left:right]
            if max(mid) >= threshold:
                temp.append(max(mid))
            # print(mid)
            left += 10
        print("temp",temp)
        if not temp :
            return
        temp = matlab.double(temp)
        res  = self.engine.gpfit(temp)

        return res



if __name__ == "__main__":
    aa = GPD()
    data = [i for i in range(20)]
    threshold = 1

    res = aa.gpd(data , threshold)

    # print(segment)
    print(res)