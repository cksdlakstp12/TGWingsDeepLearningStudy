from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange


def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    pass
    #NOTE: derivative of 'score[i,j]' with respect to 'W[k,j]' is 'X[i,k]'
    #-> derivative of 'score[i,j]' with respect to 'W[:,j]' is 'X[i]'
    # 'loss value' of 'score[i,j]' is (-ln(e^y / s)) or (ln(1+ze^(-y))), 'y' is 'score[i,y[i]]', 's' is sum of 'e^score[i]', 'z' is sum of 'e^score[i]' without 'score[i,y[i]]'.
    # derivative of 'loss value' with respect to 'x=score[i,j]' is ((e^x)/s - 1) when j is correct class.
    # derivative of 'loss value' with respect to 'x=score[i,j]' is ((e^x)/s) when j is not correct class.
    #
    # compute the loss and the gradient
    num_classes = W.shape[1]
    num_train = X.shape[0]
    loss = 0.0
    for i in range(num_train):
        scores = X[i].dot(W)
        e_scores = np.exp(scores - np.max(scores))
        sum_e_scores = np.sum(e_scores)
        loss -= np.log(e_scores[y[i]] / sum_e_scores)
        for j in range(num_classes):
            if j == y[i]:
                dW[:,y[i]] += (X[i] * (
                    e_scores[y[i]] / sum_e_scores
                    - 1
                ))
                continue
            dW[:,j] += (X[i] * (e_scores[j] / sum_e_scores))

    # Right now the loss is a sum over all training examples, but we want it
    # to be an average instead so we divide by num_train.
    loss /= num_train
    dW /= num_train

    # Add regularization to the loss.
    loss += reg * np.sum(W * W)
    dW += 2 * reg * W

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    pass
    #NOTE: derivative of 'score[i,j]' with respect to 'W[k,j]' is 'X[i,k]'
    #-> derivative of 'score[i,j]' with respect to 'W[:,j]' is 'X[i]'
    # 'loss value' of 'score[i,j]' is (-ln(e^y / s)) or (ln(1+ze^(-y))), 'y' is 'score[i,y[i]]', 's' is sum of 'e^score[i]', 'z' is sum of 'e^score[i]' without 'score[i,y[i]]'.
    # derivative of 'loss value' with respect to 'x=score[i,j]' is ((e^x)/s - 1) when j is correct class.
    # derivative of 'loss value' with respect to 'x=score[i,j]' is ((e^x)/s) when j is not correct class.
    #
    # compute the loss and the gradient
    num_classes = W.shape[1]
    num_train = X.shape[0]
    loss = 0.0
    score = X.dot(W)
    e_score = np.exp(score - np.max(score, axis=1).reshape(-1,1))
    sum_e_score = np.sum(e_score, axis=1)
    loss -= np.sum(np.log(e_score[range(num_train),y] / sum_e_score))
    tmp = np.zeros((num_train, num_classes))
    tmp[range(num_train),y] = 1
    dW += np.sum(
        np.expand_dims((e_score / sum_e_score.reshape(-1,1) - tmp), axis=1) *
        np.expand_dims(X, axis=2),
        axis=0
    )
    #This loop may be faster than above line, depends on circumstances.
    #for j in range(num_classes):
    #    dW[:,j] += np.sum(X * (
    #        (e_score[:,j] / sum_e_score).reshape(-1,1)
    #        - tmp[:,j].reshape(-1,1)
    #    ), axis=0)

    # Right now the loss is a sum over all training examples, but we want it
    # to be an average instead so we divide by num_train.
    loss /= num_train
    dW /= num_train

    # Add regularization to the loss.
    loss += reg * np.sum(W * W)
    dW += 2 * reg * W

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW
