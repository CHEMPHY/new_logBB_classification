clear
clc
X = csvread('../data/features_clean.csv',1,1);
y = csvread('../data/logBB.txt');
index = spxy(X,y,round(length(y)*0.8));
X_train = X(index,:);
y_train = y(index);
oppo_index = setdiff(1:length(y),index);
X_test = X(oppo_index,:);
y_test = y(oppo_index,:);
csvwrite('../data/x_train.csv',X_train);
csvwrite('../data/y_train.txt',y_train);
csvwrite('../data/x_test.csv',X_test);
csvwrite('../data/y_test.txt',y_test);