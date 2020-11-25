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

        # 取得是过去slice的倍数的值  并且超过阈值
        slice = 1
        segment = len(data) // slice
        data = data[ -1*segment*slice: ]
        print(data)
        temp = []
        left = -1*segment*slice
        for i in range(segment) :
            right = left + slice
            if right == 0:
                mid = data[left:]
            else:
                mid = data[left:right]
            if max(mid) >= threshold:
                temp.append(max(mid))
            # print(mid)
            left += slice
        print("temp",temp)
        if not temp :
            return
        temp = matlab.double(temp)
        # temp = []
        threshold = [threshold]
        # threshold = threshold.tolist()
        threshold = matlab.double(threshold)
        # res  = self.engine.gpfit(temp)
        ans = self.engine.gpd(temp ,threshold)
        res = ans[0][0:2]
        probability = ans[0][2]
        print(probability)
        return res,probability



if __name__ == "__main__":
    aa = GPD()
    data = [i for i in range(20)]
    threshold = 1

    res = aa.gpd(data , threshold)

    # print(segment)
    print(res)