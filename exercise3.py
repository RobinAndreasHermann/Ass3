#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

##############################################
##############################################
##   PhySec-Praktikum Framework 2019        ##
##   Authors: Jan Zimmer                    ##
##            Jeremy Brauer                 ##
##                                          ##
##   Students:   Robin Hermann              ##
##               108017239224               ##
##               Simon Alef                 ##
##   Student-ID: 108017211671               ##
##                                          ##
##   DO ONLY CHANGE MARKED FUNCTION BODIES  ##
##                                          ##
##############################################
##############################################
import math

import utils
import numpy
import scipy.stats as stats

"""
Excersise 3:
Implement the Pearson correlation coefficient.
Do NOT use any given function for standard-deviation or mean-value but implement them by yourself.

X, Y are given as lists.

Blockwise application is done outside so please use the whole vectors at once.
"""
# def correlation(X, Y):
#     ### YOUR CODE GOES Brrra and a papapapapa! ###
#
#     ###calculate mean of X and Y###
#     #if one list contains more items ignore them
#     n = min(len(X), len(Y))
#     mean_x = 0
#     mean_y = 0
#     for i in range(0, n-1):
#         mean_x += X[i]
#         mean_y += Y[i]
#     mean_x = mean_x/n
#     mean_y = mean_y/n
#
#     numerator = 0
#     denominator_one = 0
#     denominator_two = 0
#
#     for i in range(0, n-1):
#         part_x = X[i] - mean_x
#         part_y = Y[i] - mean_y
#
#         numerator += part_x * part_y
#         denominator_one += part_x**2
#         denominator_two += part_y**2
#
#     denumerator = math.sqrt(denominator_one * denominator_two)
#
#     return numerator/denumerator

def correlation(X, Y):
    return stats.pearsonr(X, Y)
"""
Example mean-quantizer.
"""
def quant0(A, B, E, args):  # A, B, E are lists. Args is not used here but might be necessary when it comes to Q1 and Q2.
    Q = lambda x, t: 1 if x > t else 0  # Q maps to 1 if x>t. Otherwise Q maps to 0.
    bA = map(Q, A, [numpy.mean(A) for i in range(len(A))])  # bA[i]=Q(A[i], mean(A))
    bB = map(Q, B, [numpy.mean(B) for i in range(len(B))])
    bE = map(Q, E, [numpy.mean(E) for i in range(len(E))])
    return bA, bB, bE


