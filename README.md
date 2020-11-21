# Data Science and Toolkits

### Milestone 4


#### 0.

Insert milestone 3 tasks here.


#### 1.

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

A metric is a way to evaluate the performance of an algorithm. For example, Accuracy as a popular metric
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

To explain AUROC (Area Under Receiver Operating Characteristics Curve), we first have to define the ROC. ROC (Receiver Operating Characteristics) curves are used to see how well a certain classifier can separate positive and negative examples and to identify the best threshold for separating them. It visualizes the tradeoff between Sensitivity (aka TPR, True Positive Rate) and FPR (False Positive rate, 1-Specificity) in a binary classifier (as can be seen in Figure 1).


![](assets/markdown-img-paste-20201121095421934.png)

Figure 1: ROC

If the ROC curve is on the diagonal line, the classifier performs no better than random guessing. The perfect classifier would hug the y-axis to the left and the top x-axis. If the ROC curve is below the diagonal, it is a bad classifier. If it is above, it is between a ok-ish and a good classifier (up to debate depending on the dataset).

AUROC is the Area under the ROC curve and basically quantifies the ROC in a number. If the AUROC is equals to 1, the classifier predicts perfectly and the classifier is able to distinguish between positive and negative classes. If the AUROC is equals to 0.5, then the classifier is no better than random guessing. If AUROC is below 0.5, then the classifier is bad. If AUROC is between 0.5 and 1, let's assume 0.7, then the classifier is able to distinguish positive and negative classes in 70% of cases.

Advantages of using ROC and AUROC:

- ROC curves can be used to evaluate the tradeoff between Sensitivity and Specificity for all possible thresholds
- Several cutoff values can be compared
- AUROC provides a single measure to compare different models


\
*What is a Confusion Matrix?*

Confusion Matrix:
|  |     | Actual | Actual |
| --- | --- | --- | --- |
|  |     | **1** | **0**
| **Predicted** |  **1**   | True Positive (TP) | False Positive (FP)
| **Predicted** |  **0**   | False Negative (FN) | True Negative (TN)

The confusion matrix shows if the classifier correctly identified the observation or was it confused with other labels?

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
 
