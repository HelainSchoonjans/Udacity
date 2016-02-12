# Udacity's deep learning #
## Introduction ##
This project contains my work doing the assignements of the deep learning class of Udacity.

## Using the tenserflow VM ##
Some exercices must be done on a Docker virtual machine image. We will see here how to mount a folder on Boot2Docker and use it with our image to save the changes we make in the image.

## Running the Tenserflow image ##
The [tutorial](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/udacity/README.md) assumes that you are using Linux and gives you no clue on how to use port forwarding with Boot2Docker. Port forwarding will enable you to access the python notebook in your browser instead of curling it from inside your VM.

To start Boot2Docker with port forwarding on port 8888:

    boot2docker up
	boot2docker ssh -L 8888:localhost:8888

You can then run the image and use your browser to see your notebook on http://127.0.0.1:8888.

## Running the image ##
A said in the tutorial, you just have to enter the following command to run the container:

    docker run -p 8888:8888 -it --rm b.gcr.io/tensorflow-udacity/assignments

To avoid losing your work between the sessions, it is recommended that you mount the tensorflow/examples/udacity directory into the container.

## Mounting a windows directory into the container ##

By default Boot2Docker seems to mount the folder *C:\Users*. If it is not the case on your Boot2Docker or if you want to mount another folder, use the [following steps](http://www.howtogeek.com/187703/how-to-access-folders-on-your-host-machine-from-an-ubuntu-virtual-machine-in-virtualbox/).

Now that you have a shared folder, you can just run the image with the folder mounted:

	run -p 8888:8888 -v </path/to/tensorflow/examples/udacity>:/notebooks -it --rm $USER/assignments

Example:

	run -p 8888:8888 -v /c/Users/hschoonjans/Documents/GitHub/Udacity/DeepLearning/tenserflow/examples/udacity/:/notebooks -it --rm b.gcr.io/tensorflow-udacity/assignments

You may notice that you have no notebooks; copy the content of tenserflow/examples/udacity to your udacity directory. You will now have access to your notebooks.
