

<img width="30%" src="./readme_imgs/psiori.png" />


# Topic: Autoencoder

With high-dimensional, complex datasets (e.g. from sensor data like in computer vision), the importance of finding the underlying significant variables increases proportionately.
Only by encoding the information in fewer dimensions, processing in real time becomes a reality and at the same time, meaningful variables can be extracted.
An autoencoder is a neural network that finds the underlying distribution using an encoder-decoder architecture where the output is trained to be equal to the input while the information passing through the network is compressed and simplified in an intermediate layer, the so-called bottleneck.


<img width="50%" src="./readme_imgs/autoencoder_architecture.png" />

There is a wide range of applications such as noise reduction, semantic hashing and image-to-position mapping.


# Challenge

In this specific challenge we provide you with images of an autonomous racing car on a carrera track, which we recorded using a top view camera. These recordings contain high-dimensional vectors, however, a one-dimensional manifold underlies this data.
We challenge you to encode the images in three dimensions by using an autoencoder. As a result you should be able to visualize the one-dimensional manifold.

<img width="80%" src="./readme_imgs/autoencoder_challenge.png" />


The benefit of dimensional reduction in image-to-position mapping is useful especially for advanced tasks such as learning to control the speed of a racing car by using reinforcement learning (Lange, S., Riedmiller, M., & Voigtländer, A., Autonomous reinforcement learning on raw visual input data in a real world application. In Proc. of IJCNN 2012).

# Dataset 

- images (1600, 304, 808, 3): RGB values: [0-255] 
	- to be used as sole input data to the neural network
- ranges (1600,): position of the car on the track: [0-2π] 
	- to be used in evaluation only

# Submission

   1. Development of model in model_development.ipynb
   
	- remark: illustrate your whole development process
	
	- remark: do not use ground truth data for optimization, it only serves for supervision enabling you to come up with new models
	
   2. Fill encode(x) function with your method in evaluate_encoded_data.ipynb

# Evaluation

Using the ground truth position data a random forest (max_depth=5, n_estimators=5) learns the mapping from embedding space to the range the car traveled from the startpoint.
The cross validation error of the mapping equals the score. For the final ranking a secret dataset with 400 data points will be used.

Our own baseline network achieved an error of 0.288 on the test set. Preprocessing of the benchmark included scaling and reshaping.

