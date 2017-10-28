# Installing with Anaconda

Taken from
https://www.tensorflow.org/install/install_mac#installing_with_anaconda

Note: for a Mac, does not use the GPU, only CPU, bummer.

The Anaconda installation is community supported, not officially supported.

Take the following steps to install TensorFlow in an Anaconda environment:

Follow the instructions on the Anaconda download site to download and install
Anaconda.
Create a conda environment named tensorflow by invoking the following command:

$ conda create -n tensorflow
Activate the conda environment by issuing the following command:

$ source activate tensorflow
 (tensorflow)$  # Your prompt should change
 Issue a command of the following format to install TensorFlow inside your
 conda environment:

 (tensorflow)$ pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.3.0-py3-none-any.whl

## Validate
# Python
>>> import tensorflow as tf
>>> hello = tf.constant('Hello, TensorFlow!')
>>> sess = tf.Session()
>>> print(sess.run(hello))

It should print lots of warnings, and also b'Hello, TensorFlow!'
>>> quit()

Bingo, bingo.
