#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 16:44:41 2019

@author: ali
"""
import sys
sys.path.insert(0, '../ReadFile')
sys.path.insert(0, '../Given')
import InputConstants
import ReadFile
class node:
    def __init__(self, name, cap, degree):
        self.name = name
        self.cap = cap
        self.degree = degree
        self.function = 'None'
    def placement(self, function):
        self.function = function
#class ServiceChain:
#    def __init__(self, )
# Main
v1 = node('node_1', 20, 3)
v2 = node('node_2', 20, 4)
input_cons = InputConstants.Inputs()
graph = ReadFile.Graph(input_cons.network_path + input_cons.network_name)
#print (IndentationError.read_path)
#Mf_cal()
        