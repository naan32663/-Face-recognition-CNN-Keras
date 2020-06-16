import os
import sys
import numpy as np
import cv2

IMAGE_SIZE = 64


def resize_image(image, height = IMAGE_SIZE, width = IMAGE_SIZE):
    top, bottom, left, right = (0, 0, 0, 0)
    
    #获取图像尺寸
    h, w, _ = image.shape
    
    #对于长宽不相等的图片，找到最长的一边
    longest_edge = max(h, w)    
    
    #计算短边需要增加多上像素宽度使其与长边等长
    if h < longest_edge:
        dh = longest_edge - h
        top = dh // 2
        bottom = dh - top
    elif w < longest_edge:
        dw = longest_edge - w
        left = dw // 2
        right = dw - left
    else:
        pass 
    
    #RGB颜色
    BLACK = [0, 0, 0]
    
    #给图像增加边界，是图片长、宽等长，cv2.BORDER_CONSTANT指定边界颜色由value指定
    constant = cv2.copyMakeBorder(image, top , bottom, left, right, cv2.BORDER_CONSTANT, value = BLACK)
    
    #调整图像大小并返回
    return cv2.resize(constant, (height, width))

#读取训练数据

images = []
labels = []
def read_path(path_name): 
#    os.chdir("drive/Colab Notebooks/Caucasian-processed") # content/drive/Colab Notebooks/Caucasian-processed
    	
    for dir_item in os.listdir(path_name):

            if dir_item.endswith('.jpg'):
                image = cv2.imread(path_name+dir_item)
                print('image name = ' + dir_item )
                image = resize_image(image, IMAGE_SIZE, IMAGE_SIZE)
                
                #放开这个代码，可以看到resize_image()函数的实际调用效果
                #cv2.imwrite('1.jpg', image)
				
				#数字化label, female=1, male=2
                str = dir_item[0:5]
                if str.startswith('CF'):
                  str = '1' + dir_item[2:5]
                else:
                  str = '2' + dir_item[2:5]
				
                images.append(image)                
                labels.append(str)                                
                    
    return images,labels
    

#从指定路径读取训练数据
def load_dataset(path_name):
    images,labels = read_path(path_name)    
    
    #将输入的所有图片转成四维数组，尺寸为(图片数量*IMAGE_SIZE*IMAGE_SIZE*3)
    #我和闺女两个人共1200张图片，IMAGE_SIZE为64，故对我来说尺寸为1200 * 64 * 64 * 3
    #图片为64 * 64像素,一个像素3个颜色值(RGB)
    images = np.array(images)
    print(images.shape)    
    
    labels = np.array(labels)    
    
    return images, labels

if __name__ == '__main__':
 
        path_name = '/content/gdrive/My Drive/Colab Notebooks/Caucasian-processed/'
        images, labels = load_dataset(path_name)