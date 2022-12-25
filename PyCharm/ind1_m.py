#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def max_min(type='max'):
    def helper(collection):
        if type == 'max':
            return max(collection)
        else:
            return min(collection)
    return helper
