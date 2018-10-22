import os

'''
模型的基本配置 
BASE_DIR 本地路径
train_path 训练路径
test_path 测试路径

'''

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#特征工程相关配置
#train_path = os.path.join(BASE_DIR, "data\\train_1w.csv")
#test_path = os.path.join(BASE_DIR, "data\\test_1k.csv")

train_data_dir=BASE_DIR + '/data'
test_data_dir=BASE_DIR + '/data'
data_dir=BASE_DIR + '/data'
output_dir=BASE_DIR +'/output'
trainfilename='train_100w.csv'
testfilename='test_10w.csv'
continous_features = range(1, 5)
categorial_features = range(5, 31)
continous_clip = [1740, 6, 2, 2] #待调整
cutoff = 30

#深度网络相关配置
#输入数据
encod_train_path=BASE_DIR + '/output/train.txt'
encod_vaild_path=BASE_DIR + '/output/valid.txt'
encod_test_path=BASE_DIR + 'output/test.txt'
encod_cat_index_begin = 4
encod_cat_index_end = 30
dictsizefile=BASE_DIR + '/output/dictsize.csv'
model_ouput_dir=BASE_DIR + '/model_output'
summary_dir=BASE_DIR + '/summary'

batch_size=1000
keep_prob=0.8
logfrequency=10
Max_step=20000000
embed_dim=128
learning_rate=0.01
oridata_dim=23




