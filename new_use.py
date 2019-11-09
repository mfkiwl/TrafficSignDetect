from keras.models import load_model
import numpy as np
import cv2


# 加载模型h5文件

class SignDetect:
    model = load_model("traffic_signs.h5")
    sign_name = {'0': '最高时速20km/h', '1': '最高时速30km/h', '2': '最高时速50km/h', '3': '最高时速60km/h', '4': '最高时速70km/h',
                 '5': '最高时速80km/h', '6': '极限时速80 km/h', '7': '最高时速100km/h', '8': '最高时速120km/h', '9': '不许超车',
                 '10': '载重超过3.5吨的车辆禁止超车', '11': '干路先行', '12': '干路', '13': '优先通过', '14': '禁止通行', '15': '禁止入内',
                 '16': '卡车禁止通行', '17': '禁止驶入', '18': '注意危险', '19': '向左转',
                 '20': '向右转', '21': '急转弯', '22': '路面颠簸', '23': '小心侧翻', '24': '右侧路面变窄', '25': '前方施工路段',
                 '26': '注意信号灯',
                 '27': '注意行人', '28': '注意儿童', '29': '注意非机动车',
                 '30': '注意下雪', '31': '注意野生动物', '32': '禁止长时间停车', '33': '右转', '34': '左转', '35': '直行', '36': '直行或右转',
                 '37': '直行或左转', '38': '靠道路右侧行驶', '39': '靠道路左侧行驶',
                 '40': '环形道路', '41': '小心并行', '42': '小心与货车并行'}

    # 规范化图片大小和像素值
    @staticmethod
    def get_inputs(src):
        input_img = cv2.imread(src)
        input_img = cv2.resize(input_img, (48, 48))
        input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB)
        pre_x = np.array([np.array(input_img) / 255.0])
        return pre_x

    # 要预测的图片保存在这里

    def do_detect(self, pdir):
        # 调用函数，规范化图片
        pre_x = self.get_inputs(pdir)
        # 预测
        pre_y = self.model.predict(pre_x)
        max_num = 0
        max_index = 0
        for index in range(len(pre_y[0])):
            if pre_y[0][index] >= max_num:
                max_num = pre_y[0][index]
                max_index = index
        return self.sign_name[str(max_index)]


