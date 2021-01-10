# Data Science and Toolkits

### Milestone 4

Repository of Bud and Thanu

### 0.

Due to time constraints, we were not able to implement the lacking parts of Milestone3. We will add those steps as soon as possible.


### 1.

*What is Experiment Management and why is it important?*

To answer this question, we need to define what exactly is meant by experiment.
Basically, in a data scientist environment, an experiment could be that one algorithm is better
than another or that with hyperparameter tuning, one such model performs better than the vanilla version.
To improve an algorithm, one can conduct several experiments and choose the one which performs best. At this point,
experiment management becomes handy since there might be a myriad of changes one could make and keeping track of each
becomes a challenge if performed manually. Forgetting which model had certain features/alterations can be detrimental
and becomes quickly confusing. Experiment management is thus necessary to keep track of all changes and alterations
to the code/database/hyperparameters etc.

\
*What is a Metric in ML?*

A metric is a way to evaluate the performance of an algorithm. For example, Accuracy is a popular metric
for machine learning algorithms. Accuracy (opposite of error rate) measures how often a certain algorithm predicts
data points correctly. It is the ratio of correctly predicted data points to all data points. More in-depth:

Accuracy is defined as the number of true positives and true negatives divided by the number of true positives,
true negatives, false positives, and false negatives.

\
*What is Precision and Recall? Why is there often a Trade-off between them?*

Precision (aka Positive Predictive Value) is the ratio of true positives (correctly predicted positive values)
to true positives plus false positives (cases which are predicted to be positive but are actually negative, Type I error) which measures the chance of
having the positive condition among those that test positive. The question regarding this ratio is:
When the classifier/algorithm predicts positive, how often is it correct?

Recall (aka Sensitivity) is the ratio of true positives to true positives plus
false negatives (cases which are predicted to be negative but are actually positive, Type II error) which measures how well the classifier/algorithm predicts positive values. The question regarding this ratio is: When the value is actually positive, how often does the classifier predict positive?


The precision and recall trade-off occurs when increasing one of the parameters (precision or recall) while keeping the model the same which leads to decreasing of the other parameter. This is possible when the threshold of the classifier/algorithm is changed for example. This circumstance is due to noise in the dataset and some positive observations which are closer to the negative class and vice versa. In essence, the classifier will always miss to classify some points. Missed classifications means that classifying from negative class to positive and vice versa. The miss rate is either compromising precision or recall and up to the set threshold level. The threshold is thus the decisive tool to tip the balance between recall and precision.


**Helpful Websites for this task:**

https://datascience-george.medium.com/the-precision-recall-trade-off-aa295faba140

\
 *What is AUROC Metric?*

To explain AUROC (Area Under Receiver Operating Characteristics Curve), we first have to define the ROC. ROC (Receiver Operating Characteristics) curves are used to see how well a certain classifier can separate positive and negative examples and to identify the best threshold for separating them. It visualizes the tradeoff between Sensitivity (aka TPR, True Positive Rate) and FPR (False Positive rate, 1-Specificity) in a binary classifier.


If the ROC curve is on the diagonal line, the classifier performs no better than random guessing. The perfect classifier would hug the y-axis to the left and the top x-axis. If the ROC curve is below the diagonal, it is a bad classifier. If it is above, it is between a ok-ish and a good classifier (up to debate depending on the dataset).

AUROC is the Area under the ROC curve and basically quantifies the ROC in a number. If the AUROC is equals to 1, the classifier predicts perfectly and the classifier is able to distinguish between positive and negative classes. If the AUROC is equals to 0.5, then the classifier is no better than random guessing. If AUROC is below 0.5, then the classifier is bad. If AUROC is between 0.5 and 1, let's assume 0.7, then the classifier is able to distinguish positive and negative classes in 70% of cases.

Advantages of using ROC and AUROC:

- ROC curves can be used to evaluate the tradeoff between Sensitivity and Specificity for all possible thresholds
- Several cutoff values can be compared
- AUROC provides a single measure to compare different models\

\
*What is a Confusion Matrix?*

Confusion Matrix:
|  |     | Actual | Actual |
| --- | --- | --- | --- |
|  |     | **1** | **0**
| **Predicted** |  **1**   | True Positive (TP) | False Positive (FP)
| **Predicted** |  **0**   | False Negative (FN) | True Negative (TN)


The confusion matrix shows if the classifier correctly identified the observation or was it confused with other labels.

- TP: Cases which are predicted to be positive and are actually positive.
- TN: Cases which are predicted to be negative and are actually negative.
- FP: Cases which are predicted to be positive but are actually negative.
- FN: Cases which are predicted to be negative but are actually positive.

The confusion matrix can be used to measure the performance of the classifier (Accuracy, Error rate). It can further be used to measure positive identifications (Recall, Fall-Out) or negative identifications (Specificity, False Negative Rate). There are further calculations to measure performance with abbreviations of the confusion matrix.

Advantages:

- Identifies critical situations.
- Offers new perspective on the performance of various classifiers.

Disadvantages:

- Does not account for unbalanced datasets (for example when 90% of observations are actually positive, thus accuracy is not representative of true performance of identifier)



### 2.

We created a public Weights & Biases project:

https://wandb.ai/bdelhees/ds-tk


*Preparing Tasks:*

Due to technical difficulties, we set up our VirtualBox from scratch with the help from Sandro.
The problem before was that the VirtualBox kept booting over the ISO-file, which lead to minimal
disk space available and thus most packages were not able to be installed. After setting up the new VirtualBox, we installed the following packages/modules which are necessary to predict bitcoin prices with our code:

- **numpy**
- **keras**
- **matplotlib**
- **sklearn**
- **TensorFlow**

While trying to install the last module, I ran into the following error message:

"Could not install packages due to an EnvironmentError: [Errno 28] No space left on device"

To check whether this is true, I ran:

```sh
df -h
```

the root folder: **/** shows only a 39% usage. **Pip3** chooses to install packages under **/usr/lib/python3/dist-packages**. To check how much disk space is used in this directory I ran:

```sh
du -sh /usr/lib/python3/dist-packages
```
It showed that 62Mb were used, which accounts for the packages **numpy**, **matplotlib** and **sklearn**. **Keras** was installed but during the (unsuccessful) installation of **TensorFlow**, **keras** has been deleted (maybe because **keras** is included in **TensorFlow**).  

I tried to delete the cache and hope that it somehow solves the problem:

```sh
sudo du -sh /usr/lib/python3/dist-packages
sudo apt-get clean
```


This did not work. I tried another approach I found on https://github.com/pypa/pip/issues/5816 :


```sh
TMPDIR=/data/bud/ pip3 install --cache-dir=/data/bud/ --build /data/bud/ tensorflow
```

This did not work either. I encountered the following Error message:

"ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/data' Check the permission"

\
\
**DISCLAIMER:**

Before we show you the further steps, we need to address that we both are not able to run our code on our Virtualmachines, which makes it impossible to see if the following steps are correct or not. Trial and Error is thus not an option. Since Sandro and Arthur recommended us to not upload faulty code to our master branch, we decided that task 2 remains on the branch bud_workon. So all our changes to the code are found the on the mentioned branch.

The tasks are as follows:

\
*0. Choose an appropriate metric for optimizing your ML Model. What is the reasoning behind
it?*

After looking at some literature regarding performance metrics for price predictions, most of the articles suggest Root Mean Square Error (RMSE) values. However, in our code the loss is already defined as MSE (Mean Squared Error).


\
*1. Login to W&B (Tip: you can use ENTRYPOINT in a Dockerfile to run a shell
script that logs you in (see below))*

First step:
```sh
pip3 install wandb
```

After that, we tried to login via to see if it works without a dockerfile:

```sh
wandb login "super special secret code which we cannot share here"
```
This worked. To include weights and biases in our script, we added the following lines to our **loading_and_preparing_data.py** script:

```sh
import wandb
from wandb.keras import WandbCallback

wand.init(project='wandb-dstk',
          group="experiment1"
          config ={
                "epochs": 100,
                "batch_size": 5,
                "loss": "MSE"
                "architecture": "RNN"
                "dataset": "bitcoin.csv"
                })

config = wandb.config

```

Since we are not able to run the code (see DISCLAIMER) and thus a Dockerfile is redundant, we still thought about how we would approach this (shoutout to Vitor and Michaela).

To run the model on docker, we first created a docker file:

```sh
FROM python:3.8.3

WORKDIR /home/Desktop/mendicantbias

COPY . /home/Desktop/mendicantbias

RUN pip install -U pip
RUN pip install -r requirements.txt

ENTRYPOINT ["bash","docker_entrypoint.sh"]

CMD python3 main.py
```

The entrypoint script is as follows:

```sh
#!/bin/bash
set -e

wandb login $WANDB_TOKEN

exec "$@"
```


\
*2. Train a Model*

Now we have to extend our code and thus model, so that weights and biases can access it and save it. We inserted this code to the **rnn_layer_fitting.py** :

```sh
regressor.compile(optimizer=config.optimizer,
              loss=config.loss
              )

history = model.fit(x=X_train,
                    y=y_train,
                    epochs=config.epoch,
                    batch_size=config.batch_size,
                    validation_data=(test_set),
                    callbacks=[WandbCallback()])
```

\
*3. Save and upload the trained model*

To save the model we insert,

```sh
wandb.finish()
```

to the end of the **rnn_layer_fitting.py** file.


\
*4. Log the value of the loss function (graphically)*

Next, we log a run, using the same experiment name as the group parameter so that this run and the previous run are grouped together in W&B. We inserted the following code to the prediction.py script:

```sh
wandb.init(project="wandb-dstk", group=experiment1)


wandb.log({"predicted BTC Prices": predicted_BTC_prices})

print(predicted_BTC_prices)
print(test_set)
```
\
*5. Log your metric (graphically), Tip use a Keras Metric*


See 4.


\
*6. Try to play with your Neural Network, by changing parameters or even its
architecture. Make sure that you log those changes automatically to W&B. Compare
the runs on W&B, how do the metrics/loss change?*

See Disclaimer

**Helpful Websites for this task:**

https://www.wandb.com/tutorial/recurrent-neural-networks

https://colab.research.google.com/drive/1aEv8Haa3ppfClcCiC2TB8WLHB4jnY_Ds#scrollTo=8yrgPBRXrvx2




### 3.
\
To create a Jupyter notebook, we executed the following commands:

```sh
# first, always upgrade pip!
pip install --upgrade pip
pip install --upgrade ipython jupyter
```
\
Then we start the notebook in the tutorial directory:


```sh
cd ipython-in-depth
jupyter notebook
```
\
After that, we used the following command:

```sh
jupyter notebook –allow root
```
\
Which gives you the information about the localhost , where it is running and so on. We need to open the browser, then we can see the folder.
