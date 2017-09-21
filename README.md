# Summer-2017

Summer Research for birds species classcification and birds location detection with Dr.Barnett

I used convolutional neural network to indentify the birds species of given image dataset and detect . 

train_CNN.py:

This file is used for training the input images with size 140*140 into the different layers of CNN. You can test the VGG 16, VGG 19 and 4/6 layers of CNN. It used the learning rate decay function. If test the fixed learning rate, modify the lr_schedule function.


train_frcnn.py:
This file will parse the annotation.txt as input and read all the positions and file names to import image and pre-bounding box location. Then using those images and location for the FRCNN training. The supporting paper and code is list in here:
https://arxiv.org/abs/1506.01497 
https://github.com/yhenon/keras-frcnn.


FRCNN file is the basic frame work of FRCNN and I made some modifies in those files other than the orginanl one.


label_pointer.py: used for labeling the create bounding box areas for the birds images. 


Training images can be find in website:http://www.mathcs.richmond.edu/~lbarnett/research/summer2017/index.php. All years images files are used for train_CNN.py, bird/Nobird files are used for FRCNN but we need to prelabel the bounding box.
