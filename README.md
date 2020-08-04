# How to use the pipeline?

#### Important note:

I am assuming that 2D Object Detection Network selected is finalised. I have selected Single Shot Detector with MobileNet which can be used in real-time application.

The instructions below will be assuming that the task of future members is to only:

0. Download the pipeline that was set up.
1. Collect more quality training and testing images.
2. Labelled the newly collect images.
3. Retrain the network.


## 0. Download the pipeline.

Please download the folders over at [Google Drive]().


## 1. Collect data

The current data collected,labelled and train on can be found at `models/research/object_detection/images/train`.

To date (2020), the RobotX team has not collected any quality images at prior competitions. Please attempt to collect more images with the boat on the water. It will be especially useful to gather lots of images from the competition itself if the organiser permits time for trial runs. You can then take all of these images, labelled them and retrain. Algorithm will work super well if the data collected is similar/exactly like the competition scene.

Add the training images that you have collected to the folder `object_detection/images/train`, testing images into `object_detection/images/train`.

## 2. Label the images

Follow this github instruction, [here](https://github.com/tzutalin/labelImg) to download the labelling application

The application will produce `*.xml` files for each of your labelled images. Once you are done labelling, we will need to convert all of the `*.xml` files to an excel spreadsheet. This can be done by running `xml_to_csv` (object_detection/images) which creates `train_labels.csv` and `test_labels.csv`. `*.xml` files has to be converted into TFRecords for Tensorflow to train the network. Go to `line 32 generate_tfrecord.py` and add the objects label.

In terminal (Ensure u are in path: models/research/object_detection): 

To create train data record for tensorflow:

```
python generate_tfrecord.py --csv_input=images/train_labels.csv --image_dir=images/train --output_path=train.record
```

To create test data record for tensorflow:

```
python generate_tfrecord.py --csv_input=images/test_labels.csv  --image_dir=images/test --output_path=test.record

```

## Retrain

I have set up an easy to use *.ipynb script that is suppose to work "out of the box". The reason why I set it up to be a *.ipynb script is so that you can use Colaboratory to train (free of charge cloud GPU offered by Google), roughly 12 hours of free runtime.

Save the whole folder `models` into your google drive. Run `training_custom_object_detection.ipynb` to train. The notebook will export the newly train frozen graph containing the entire neural network model with all of its parameters once training is done. To run the inference, all you will need is the frozen trained model with the ssd model folder and the label_map.pbtxt. 

Check out `inference.ipynb` to learn how to run the inference and check the inference speed. This will be the "final" script to be run in real-time for the embedded hardware with the camera.

**last step: need more research into how to use opencv to parse images in real-time and throw into the network.


# Dependencies:

Tensorflow 1.x, Python 3.7
