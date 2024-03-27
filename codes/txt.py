import os
from os import getcwd

#def getfilename(wd):
#    classes = os.listdir(wd)
#    return classes

#if __name__ == "__main__":
#    wd = 'E:\\Users\\peter\\Desktop\\uiuc\\STAT542\\VGGNet\\vggmast-master\\train'  # 替换为您的实际文件夹路径
#    classes = getfilename(wd)
#    print(classes)

classes=['antelope', 'badger', 'bat', 'bear', 'bee', 'beetle', 'bison', 'boar', 'butterfly', 'cat', 'caterpillar', 'chimpanzee', 'cockroach', 'cow', 'coyote', 'crab', 'crow', 'deer', 'dog', 'dolphin', 'donkey', 'dragonfly', 'duck', 'eagle', 'elephant', 'flamingo', 'fly', 'fox', 'goat', 'goldfish', 'goose', 'gorilla', 'grasshopper', 'hamster', 'hare', 'hedgehog', 'hippopotamus', 'hornbill', 'horse', 'hummingbird', 'hyena', 'jellyfish', 'kangaroo', 'koala', 'ladybugs', 'leopard', 'lion', 'lizard', 'lobster', 'mosquito', 'moth', 'mouse', 'octopus', 'okapi', 'orangutan', 'otter', 'owl', 'ox', 'oyster', 'panda', 'parrot', 'pelecaniformes', 'penguin', 'pig', 'pigeon', 'porcupine', 'possum', 'raccoon', 'rat', 'reindeer', 'rhinoceros', 'sandpiper', 'seahorse', 'seal', 'shark', 'sheep', 'snake', 'sparrow', 'squid', 'squirrel', 'starfish', 'swan', 'tiger', 'turkey', 'turtle', 'whale', 'wolf', 'wombat', 'woodpecker', 'zebra']
sets=['train']

if __name__=='__main__':
    wd=getcwd()
    for se in sets:
        list_file=open('cls_'+ se +'.txt','w')

        datasets_path=se
        types_name=os.listdir(datasets_path)#os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
        for type_name in types_name:
            if type_name not in classes:
                continue
            cls_id=classes.index(type_name)#输出0-1
            photos_path=os.path.join(datasets_path,type_name)
            photos_name=os.listdir(photos_path)
            for photo_name in photos_name:
                _,postfix=os.path.splitext(photo_name)#该函数用于分离文件名与拓展名
                if postfix not in['.jpg','.png','.jpeg']:
                    continue
                list_file.write(str(cls_id)+';'+'%s/%s'%(wd, os.path.join(photos_path,photo_name)))
                list_file.write('\n')
        list_file.close()




