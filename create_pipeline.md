# Creating 2D Object Detection Pipeline:


## 1. Selection of algorithm network

This can be done by downloading a pre-trained network from [Tensorflow Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md).After downloading the network file u want, untar/unzip.

## 2. Arrangement of folders

Git clone [Tensorflow Object Detection API](https://github.com/tensorflow/models)
The only important folder you need is `models`.

a) Go to models -> research -> object_detection (*Move the folder u downloaded from step 1 here)

b) object_detection -> images -> train (Go to next step)

This location will be your main workspace.

## 3. Training and Testing Data

In `models/research/object_detection/`, create an empty folder (I personally name it `images`). In `images`, create two folder (`train`,`test`) for training and testing images.

Add the training images that you have collected to the folder (`object_detection/images/train`), testing images into `test`.

## 4. Label the images

Follow this github instructio [here](https://github.com/tzutalin/labelImg) to download the labelling application.

The application will produce `*.xml` files for each of your labelled images. Once you are done labelling, we will need to convert all of 
the `*.xml` files to an excel spreadsheet. This can be done by running `xml_to_csv.py` (object_detection/images) which creates `train_labels.csv` 
and `test_labels.csv`. `*.xml` files has to be converted into TFRecords for Tensorflow to train the network.Go to `line 32 generate_tfrecord.py`
and add the objects label.

`xml_to_csv.py` and `generate_tfrecord.py` is written by a 3rd party, you can get it from the pipeline that I have shared with you and transfer the
scripts according to the location I have specify.

In terminal (Ensure u are in path: `models/research/object_detection`): 

To create train data:

```
python generate_tfrecord.py --csv_input=images/train_labels.csv --image_dir=images/train --output_path=train.record
```

To create test data:

```
python generate_tfrecord.py --csv_input=images/test_labels.csv  --image_dir=images/test --output_path=test.record

```

## 5. Setting up custom configuration

Go to -> models -> research -> object_detection -> training and edit the `line 22 pbtxt_generation.py`, add in your labels according to the order which u edit `generate_tfrecord.py`. `pbtxt_generation.py` will create `label_map.pbtxt` which will be used to refer to the objects label in training and inference.

Find the config file for your chosen network [here](https://github.com/tensorflow/models/tree/master/research/object_detection/samples/configs), 
move the .config file into the `training` folder and edit the .config file:

a) Change the number of classes
b) Change the data augmentation options as u see fit (More info: [here](https://github.com/tensorflow/models/blob/master/research/object_detection/protos/preprocessor.proto ) and [here](https://github.com/tensorflow/models/blob/master/research/object_detection/core/preprocessor.py).

Example: adding this line (you can see in the .config file in /training how it is being added):
```
data_augmentation_options {
  random_adjust_brightness {
   }
}
```

c) Change the path for `fine_tune_checkpoint` according to the folder name of your chosen network.
d) Change the number of steps in `num_steps` as u see fit.
e) Change the number of examples according to the number of training examples (object_detection/images/train).


## 6. Train and test.

I have set up an easy to use *.ipynb script that is suppose to work "out of the box". The reason why I set it up to be a *.ipynb script is so that you can use Colaboratory to train (free of charge cloud GPU offered by Google), roughly 12 hours of free runtime.

Run `training_custom_object_detection.ipynb` to train. The notebook will export the newly train frozen graph containing the entire neural network model with all of its parameters. To run the inference, all you will need is the frozen trained model with the ssd model folder and the label_map.pbtxt. 

Check out `inference.ipynb` to learn how to run the inference and check the inference speed. This will be the "final" script to be run in real-time for the embedded hardware with the camera.

**last step: need more research into how to use opencv to parse images in real-time and throw into the network.



# Dependencies:
*Important note: Pipeline was created before TF2 was released for the API. * 

Tensorflow 1.x, Python 3.7.
