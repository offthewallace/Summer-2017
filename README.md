# Summer-2017

Summer Research of machine learning method for birds species classification and birds location detection with Dr.Barnett

The program is written by Python and Keras as deep learning tool. The backend is Tensorflow and trained in Amazon-EC2.

I used convolutional neural network to identify the birds species of given image dataset and detect the positions of the birds by FRCNN implementation . The accuracy is over 97 percent for bird species classification and over 85 percent for predicting the location of bounding box for birds detection in the given images.

train_CNN.py:

This file is used for training the input images with size 140*140 into the different layers of CNN. You can test the VGG 16, VGG 19 and 4/6 layers of CNN. It used the learning rate decay function. If test the fixed learning rate, modify the lr_schedule function.

training data for CNN:https://richmond.box.com/s/34y4nxh6q85ipzw69h5lpvn8en5jq4gz


train_frcnn.py:
This file will parse the annotation.txt as input and read all the positions and file names to import image and pre-bounding box location. Then using those images and location for the FRCNN training. The supporting paper and code is list in here:
https://arxiv.org/abs/1506.01497 

https://github.com/yhenon/keras-frcnn.

training data for FRCNN:http://www.mathcs.richmond.edu/~lbarnett/research/data_sets/Bird_NoBird.tgz

FRCNN file is the basic frame work of FRCNN and I made some modifies in those files other than the orginanl one.


label_pointer.py: used for labeling the create bounding box areas for the birds images. 


Training images can be find in website:http://www.mathcs.richmond.edu/~lbarnett/research/summer2017/index.php. All years images files are used for train_CNN.py, bird/Nobird files are used for FRCNN but we need to prelabel the bounding box.
