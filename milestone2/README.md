
# Data Science and Toolkits

### Milestone 2

Repository of Bud and Thanu

#### 1.
We realized that, after the creation of the gitignore file, we could enter the gitignorefile via github. So we think it is a possibility to do the changes via github. Before starting working with the projects, we can just use the command git pull (using masterbranch) to see if changes have been made. There was also a problem which I want to mention. Bud created the gitignore file. After Thanu uses the git pull command, to stay up to date, the file was not visible in his machine. So that’s the reason behind, why we would like to use github to commit in the gitignore file.

#### 2.
##### Hashes
Hashing is the process of making files unreadable. If you then execute the file, the result is always the same. Hash functions can be used for e.g. passwords. If an unauthorized person has access, it is difficult for this person to recover passwords using the hashes.\
Hashes can also be used to identify files. The hash function generates an arbitrary input and puts a fingerprint on it, so that each change to the file changes the fingerprint. That process is basically the commit function and ensures the integrity of the file. If I run a hash function passing an entire file it will always produce the same output. This is particularly useful when distributing software.
Another common use of the hash function is partitioning file (very complex).\
The hashes allow the identification of the changes made. A hash is created for each change made. This way e.g. objects can be looked up quickly. These hashes can then also be split.

##### Modules/Package/Script
Modules and Python scripts are source code files with the extension ***.py***

Under this assumption Python scripts can be considered as modules. But there are modules which only consist of help functions. Usually modules are used to structure (organize and keep clean) large software projects. Modules must be installed before they are loaded. Since modules in Python have partly big names, an alias can be used. ( import numpy as np). Afterwards the alias can be used in Python to call functions from the module. Modules are in itself conclusive and thus work by themselves. This is because code should be built on a modular basis to tackle the problem step by step (see modular Programming).\
Packages are several modules which work together and are then combined in a package. You can also load single module from a package.\
Scripts are used to create code and are the lowest in the hierarchical structure.\
To sum up, scripts are the lowest building block which get repackaged into modules which then again get repackaged in larger packages thus creating a hierarchical structuring.

##### Docker
Explaining the difference between thick container and volume to a child, we would like to quote Arthur.  A docker container is a closed container that contains toys. Volume is a hole that allows toys to be put inside or taken out of the container.

##### Docker or Virualenv
A virtual environment only encapsulates Python dependencies. A Docker container encapsulates an entire OS. With a docker image, the whole operating system can be outsourced to another OS where Python can be installed and run on.\
The advantage of virtualenv is that you can easily switch between Python versions and dependencies. But the host system remains the same.\
Therefore, Docker is closer to a virtual machine than the virtualenv and to see if applications work on other OS, Docker would be the preferred alternative to ensure that the apps remain OS agnostic. For smaller scale tests, the virtualenv is more beneficial. Thus, the choice depends on the complexity of the task/code.

##### What is the Docker build process?
A build’s context is the set of files located in the specified PATH or URL. The build process can refer to any of the files in the context. For example, your build can use a COPY instruction to reference a file in the context. https://docs.docker.com/engine/reference/commandline/build/#:~:text=The%20docker%20build%20command%20builds,a%20file%20in%20the%20context

##### How can you asses the quality of a python package on PYPI?
Pypi offers explanations or an introduction to the individual packages of Python. It also has a githhub statistic. These show how often they were downloaded or how well they are received by the users. These statistics can be used to evaluate the file. For example, the number of stars a package received are a good indicator of its quality.

#### 3.
Note saving models request that you have the h5py library installed:
```sh
Sudo pip install h5py
```

Save your Neural Network Model to JSOn.\
The model and weight data is loaded from the saved files and a new model is created. It is important to compile the loaded model before it is used. This is so that predictions made using the model can use the appropriate efficient computation from the Keras backend.\
The model is evaluated in the same way printing the same evaluation score.

One problem which we had already in the milestone 1 was, that our virtualmachines crashed sometimes. We both switch to other computers with higher capacity (RAM, CPU etc.) for the upcoming projects and hope that this solves the problem. The real Bitcoin value can be plotted but we still have error terms when we predict future bitcoin prices with the model. The prediction is wrongly plotted as a line. We have not found a solution on github so far. Thanu talked to Arthur about it and he meant that the code should technically work. We try to solve the problem in the coming week after switching to our new computers (we both used Microsoft Surfaces, maybe there is a problematic interaction with the virtualmachines).

#### 4.
When splitting code bases into modules, there has to be onemain.py script that calls the code in all the other modules. This is the script that you call with the python command:

- 1-12: loading_and_preparing_Data.py
- 13-25: process_data.py
- 26-38: Rnn_layer_fitting.py
- 39-45: prediction.py
- 47-63: visualization_results.py

We split the code according to its main tasks. This modularization ensures that we can separately work on each module with its designated task if something does not work.

We try to make modules which make sense (at least for us). We oriented us on the structure given by the original author. After the call with Sandro, we had to fix some stuff. For example, we put all the import statements at the beginning. We did not do that for the milestone 1 because we got our brain washed with R. In R you usually import the packages just before the use of them. First we have the module loading_and_preparing_data. This includes the import of the data and also all required packages. The second module is called process_data. Here we are processing the data. The third module is called Rnn_layer_fitting, here we are initializing the RNN, added the input layer and the LSTM layer, added the output layer, compiled the RNNregressor and fitted the RNN to the Training set. The next module is called prediction, which should be self-explanatory. The last module is called visualization_results, here we are just using the commands for plotting. I want to point out, that we tried to make the module as small (number of lines) as possible and tried to group them that they make sense. We thought about splitting the module Rnn_layer_fitting even further. But we did not do that, because we think that the modules (codes) would be to small. I also think by using modules it is easier to find codes, which are not working. If we run the main module, it shows where the error happened. It is easier for a programmer to detect wrong or not working codes inside a smaller codebase. One thing that happened by running the modules was that a pycache file was created, with should allow us to run the code faster.

#### 5.
Virtualvenv is included in the Python standard library and therefore we do not need to install it. The virtualenv should be created in the same folder where the data is stored.

- To install virtualenv run:
```sh
python3 -m pip install --user virtualenv
```
- To create a virtualenv (different projects):
```sh
python3 -m venv env
```

The second argument is the location to create the virtual environment. Generally, you can just create this in your project and call it env.
venv will create a virtual Python installation in the env folder.

Note:
You should exclude your virtual environment directory from your version control system using .gitignore or similar.

- Before starting, we need to activate virtualenv:
```sh
source env/bin/activate
```

You can confirm you’re in the virtual environment by checking the location of your Python interpreter, it should point to the env directory or the anme of the virtualenv is in brackets, e.g. (virtualenv).

- On macOS and Linux:\
```sh
which python.../env/bin/python
```

As long as your virtual environment is activated pip will install packages into that specific environment and you’ll be able to import and use packages in your Python application.

- If you want to switch projects or otherwise leave your virtual environment, simply run:\
```sh
deactivate
```

##### Installing packages
- Now that you’re in your virtual environment you can install packages. Let’s install the Requests library from the Python Package Index (PyPI):
```sh
pip install requests
```

##### Freezing dependencies:
- Pip can export a list of all installed packages and their versions using the freeze command:
```sh
pip freeze
```

##### pip requirement file
first we have to create a virtualenv then activate it, then we can use pip to install the dependencies/ packages needed (be careful, check if your in the env).

#### 6.
To dockerize, we ran the following commands:
```sh
sudo apt-get update
sudo apt install docker.io
```
Docker service needs to be setup to run at startup.
```sh
sudo systemctl start docker
sudo systemctl enable --now docker
sudo usermod -aG docker ${USER}
```
Check Docker version (optional)
```sh
Docker –version
```

Initially, we got our permission denied when trying to connect to the docker deamon socket. We were able to solve this by running:
```sh
newgrp docker
```

Then we downladed a Docker image (nginx alpine, which is hopefully not malicious):
```sh
docker create --name nginx_base -p 80:80 nginx:alpine
```

We inspected our running docker images (which were hello-world and nginx_alpine):
```sh
docker images
```

Inspect containers:
```sh
docker ps -a
```

Then we tried to start the container with:
```sh
docker start nginx_base
```

However, we were not able to access the container. Might have to do with the hello-world container which is also running. The hello-world container worked though.


Sidenote: We accidentily deleted our previous files on the master branch (Milestone1) while merging. We restored the files however.
