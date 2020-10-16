
# Data Science and Toolkits

### Predicting Bitcoin Prices

Repository of Bud and Thanu

Our project aims to predict future Bitcoin prices with historical time series data. Therefore, this project utilises a Recurrent Neural Network (RNN). The prediction $y_{t}$. depends on previous input (x_t-1) and output/prediction (y_t-1). There are different RNNs. There are RNNs which use past and future values (Bidirectional RNNs). Here the values are stored one above the other. The output is then calculated based on the hidden state of both RNNs. With Deep Bidirectional RNN we have several layers per time step. This requires a lot of training data. But this leads to a higher learning capacity.
Another important aspect of this project is the LSTM Cell (which represent a single neuron). This serves the creation or learning of artificial intelligences. LSTM use a different function than the RNNS to calculate the hidden state. As memory the LSTM uses cells that take as input the previous state (y_t-1) and the current input (x_t). The cell decides itself what is stored or deleted in the cell. This type of calculation/prevision has proven to be very efficient for long term dependencies. The repeat module in an LSTM contains four interacting layers.

1)\
Based on the description of the project, it is a regression problem. The data is used to predict the price of the Bitcoins and to predict the change of the Bitcoins.
The data are time series data (discrete). The Project uses the data to determine a prediction (trends).

2)\
The author used Python version 3.0 for programming. Used packages are numpy, pandas and from matplotlib pyplot (to visualize). Furthermore Keras was used (keras.model->Sequential, keras.layers->Dense, keras.layers LSTM). Further, the TensorFlow Machine Learning library was utilized.

3) \
A new branch was created (thanu_worked_on) . On this branch the Python file as well as the data set were added and committed. Previously the whole repo was cloned from the task and the unneeded files (here README.md) were deleted. Problems arose during the login of the global user. This problem could be solved with google.

4) \
To execute the code, pip must be installed first. With the help of pip we can then install the packages needed to execute the code in the ubuntu terminal. This must be done before the code is executed. We worked with Python 3.8.5 (default) .

One problem was that the file could not be read directly from the console (python3 ./bicoin.py) . it shows that the sample is 0. If you copy all code from the bitcoin.py file and paste it into the console, the code will work.


5) \
coding: What is the code doing
1. Import
  - The necessary packages are imported.
  - The dataset is read.
  - The timeseries variable is being transformed to seconds.
  - The dataset is split to a training and test set with a prediction horizon of 30 days.
  - training set data is being processed by reshaping it.

2. Scaling Data
  - MinMaxScaler package is importet from sklear.processing
  - training set is transformed
  - training set is further splitted and its length adjusted

3. Reshape for keras
  - previously attained x training set is reshaped

4.  RNN Layers
  - import of keras libraries and packages
  - adjusting the regressor variable to sequential
  - Adjusting the RNN regarding its parameter by adding input layers to the regressor
  - adding the output layer
  - optimizing the RNN regressor
  - fitting the RNN regressor to the training set = train the RNN model

5. Making Predictions
  - exchange the training set with the test set
  - reshape the test set that it has the same properties as the training set
  - let the trained regressor/RNN model make predictions on the test set

6. Visualize the output/results

Summary:\
The input for the RNN is the training as well as the test data set which were split after the csv-file was imported which contains the bitcoin prices at a given time. The dataset was imported via pandas.
Keras is a neural network library whereas tensorflow is an open-source library containing numerous different machine learning packages not just neural networks. Keras runs on top of tensorflow which is thus required for effectively utilizing keras.

6.) \
Step 1: Update Python to 3.8.5 (default version of Ubuntu 20.04)\
Step 2: Install pip in the terminal with sudo apt install pip \
Step 3: Clone our github Repository https://github.com/BDelhees/mendicantbias to get access to the code (bitcoin.py) and the dataset (bitcoin.csv) \
Step 4: Install matplotlib, pandas, numpy, scikitlearn, TensorFlow, keras (possible that it is already included in TensorFlow) \
Step 5: To run the code in the terminal: python3 bitcoin.py \

Further problems were that the ubuntu virutalbox crashed several times and rerunning the backed up version let to further crashes. Everytime we wanted to rerun the code via the terminal, we had to clone our Repository from Github, reinstall git and pip and all necessary packages. Also, we were not able to install TensorFlow on the virtualbox. TensorFlow is a large file and even by partioning a larger space of the harddisk to the virtualbox, it was unable to install TensorFlow fully. \

9.) \
We merged the dataset unlitarerally without a pull request from the Github Repository. We worked together in person side by side so it was unnecessary to make a pull request.
