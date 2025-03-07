# encoding: utf-8
"""
Post processors operate on the output from a main processor.
They are used using the same interface as a main processor ``process``
but they accept the result of the previous step as part of the ``process`` signature.
"""
__author__ = "Richard Smith"
__date__ = "28 May 2021"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
__contact__ = "richard.d.smith@stfc.ac.uk"
