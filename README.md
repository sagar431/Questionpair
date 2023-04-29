# Quora Question Pairs - Duplicate Question Identification

## Business Problem 

### Description 

Quora is a platform for people to ask questions and get answers from the community. However, sometimes users ask similar questions or ask questions that have already been asked and answered. This can lead to frustration for users who have to search for the best answer, and for writers who have to answer the same question multiple times. To address this issue, Quora wants to identify which questions are duplicates of questions that have already been asked.

### Problem Statement 

The goal of this project is to predict whether a pair of questions on Quora are duplicates or not. This can help to provide instant answers to questions that have already been answered and reduce the time spent searching for answers.

### Sources/Useful Links

- Kaggle competition page: https://www.kaggle.com/c/quora-question-pairs
- Discussions: https://www.kaggle.com/anokas/data-analysis-xgboost-starter-0-35460-lb/comments
- Kaggle Winning Solution and other approaches: https://www.dropbox.com/sh/93968nfnrzh8bp5/AACZdtsApc1QSTQc7X0H3QZ5a?dl=0
- Blog 1: https://engineering.quora.com/Semantic-Question-Matching-with-Deep-Learning
- Blog 2: https://towardsdatascience.com/identifying-duplicate-questions-on-quora-top-12-on-kaggle-4c1cf93f1c30

### Real world/Business Objectives and Constraints 

- Misclassification is costly, so the model should have high accuracy
- Probability of a pair of questions being duplicates is needed to choose a threshold
- No strict latency concerns
- Interpretability is partially important

## Machine Learning Problem 

### Data 

#### Data Overview 

The data for this project is contained in a file called Train.csv, which contains 5 columns:

- qid1: ID of the first question in the pair
- qid2: ID of the second question in the pair
- question1: text of the first question
- question2: text of the second question
- is_duplicate: whether the pair is a duplicate or not (1 or 0)

The size of Train.csv is 60MB, and it contains 404,290 rows.

#### Example Data Point 

|id|qid1|qid2|question1|question2|is_duplicate|
|---|---|---|---|---|---|
|0|1|2|What is the step by step guide to invest in share market in india?|What is the step by step guide to invest in share market?|0|
|1|3|4|What is the story of Kohinoor (Koh-i-Noor) Diamond?|What would happen if the Indian government stole the Kohinoor (Koh-i-Noor) diamond back?|0|
|7|15|16|How can I be a good geologist?|What should I do to be a great geologist?|1|
|11|23|24|How do I read and find my YouTube comments?|How can I see all my Youtube comments?|1|

### Mapping the Real World Problem to an ML Problem 

#### Type of Machine Learning Problem 

This is a binary classification problem, where we need to predict whether a pair of questions are duplicates or not.

#### Performance Metric 

The performance metric for this project is log loss, also known as logistic loss or cross-entropy loss. Log loss measures the uncertainty of the predicted probabilities for each instance by comparing them to the true class labels.
