import numpy as np
import xgboost as xgb

X_train = np.load('X_train.npy')
y_train = np.load('y_train.npy)

model = xgb.XGBRegressor(eta=0.1, num_estimators=100, max_tree_depth=2
  tree_method=hist, n_jobs=-1)
model.fit(X_train, y_train)

         \item \texttt{max_depth}: maximum depth of a tree
            \item \texttt{gamma}: minimum loss reduction required to make a partition on a leaf node
            \item \texttt{reg\_lambda} or \texttt{reg\_alpha}: L2 (resp. L1) penalty term on weights