from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange


def svm_loss_naive(W, X, y, reg):
    """
    Structured SVM loss function, naive implementation (with loops).

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
    dW = np.zeros(W.shape)  # initialize the gradient as zero

    # compute the loss and the gradient
    num_classes = W.shape[1]
    num_train = X.shape[0]
    loss = 0.0
    for i in range(num_train):
        scores = X[i].dot(W)
        correct_class_score = scores[y[i]]
        lossAffectCount = 0
        for j in range(num_classes):
            if j == y[i]:
                continue
            margin = scores[j] - correct_class_score + 1  # note delta = 1
            if margin > 0:
                loss += margin
                #CASE OF: derivative of 'loss value' with respect to 'score[i,j]' is 'score[i,j]'
                #derivative of 'score[i,j]' with respect to 'W[:,j]' is 'X[i]'
                dW[:,j] += X[i]
                lossAffectCount += 1
        pass
        #Handle case: derivative of 'loss value' with respect to 'score[i,j]' is '-lossAffectCount * score[i,j]'
        #derivative of 'score[i,j]' with respect to 'W[:,j]' is 'X[i]'
        dW[:,y[i]] += (-lossAffectCount * X[i])

    # Right now the loss is a sum over all training examples, but we want it
    # to be an average instead so we divide by num_train.
    loss /= num_train
    dW /= num_train

    # Add regularization to the loss.
    loss += reg * np.sum(W * W)
    dW += 2 * reg * W

    #############################################################################
    # TODO:                                                                     #
    # Compute the gradient of the loss function and store it dW.                #
    # Rather that first computing the loss and then computing the derivative,   #
    # it may be simpler to compute the derivative at the same time that the     #
    # loss is being computed. As a result you may need to modify some of the    #
    # code above to compute the gradient.                                       #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    pass
    #NOTE: derivative of 'score[i,j]' with respect to 'W[k,j]' is 'X[i,k]'
    #-> derivative of 'score[i,j]' with respect to 'W[:,j]' is 'X[i]'
    # derivative of 'loss value' with respect to 'score[i,j]' is (0 or 'score[i,j]' or '-lossAffectCount * score[i,j]')

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW


def svm_loss_vectorized(W, X, y, reg):
    """
    Structured SVM loss function, vectorized implementation.

    Inputs and outputs are the same as svm_loss_naive.
    """
    loss = 0.0
    dW = np.zeros(W.shape)  # initialize the gradient as zero

    #############################################################################
    # TODO:                                                                     #
    # Implement a vectorized version of the structured SVM loss, storing the    #
    # result in loss.                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    pass
    #NOTE: derivative of 'score[i,j]' with respect to 'W[k,j]' is 'X[i,k]'
    #-> derivative of 'score[i,j]' with respect to 'W[:,j]' is 'X[i]'
    # derivative of 'loss value' with respect to 'score[i,j]' is (0 or 'score[i,j]' or '-lossAffectCount * score[i,j]')
    dW = np.zeros(W.shape)  # initialize the gradient as zero

    # compute the loss and the gradient
    num_classes = W.shape[1]
    num_train = X.shape[0]
    loss = 0.0
    score = X.dot(W)
    margin = score + 1
    correct_class_score = np.zeros((num_train, ))
    for i in range(num_train):
        margin[i,y[i]] = correct_class_score[i] = score[i,y[i]]
    margin -= correct_class_score.reshape(-1, 1)
    #
    for j in range(num_classes):
        view = margin[:,j]
        mask = view > 0
        #Handle case: derivative of 'loss value' with respect to 'score[i,j]' is 'score[i,j]'
        #derivative of 'score[i,j]' with respect to 'W[:,j]' is 'X[i]'
        dW[:,j] += np.sum(X[mask], axis=0)
        #loss value update
        loss += view[mask].sum()
        pass
    #Handle case: derivative of 'loss value' with respect to 'score[i,j]' is '-lossAffectCount * score[i,j]'
    #derivative of 'score[i,j]' with respect to 'W[:,j]' is 'X[i]'
    margin[margin > 0] = 1
    margin[margin < 0] = 0
    tmp = (np.sum(margin, axis=1).reshape(-1,1) * X)
    for i in range(num_train):
        dW[:,y[i]] -= tmp[i]

    # Right now the loss is a sum over all training examples, but we want it
    # to be an average instead so we divide by num_train.
    loss /= num_train
    dW /= num_train

    # Add regularization to the loss.
    loss += reg * np.sum(W * W)
    dW += 2 * reg * W

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    #############################################################################
    # TODO:                                                                     #
    # Implement a vectorized version of the gradient for the structured SVM     #
    # loss, storing the result in dW.                                           #
    #                                                                           #
    # Hint: Instead of computing the gradient from scratch, it may be easier    #
    # to reuse some of the intermediate values that you used to compute the     #
    # loss.                                                                     #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW
