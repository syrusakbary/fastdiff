#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `fastdiff` package."""

import pytest


from fastdiff import compare
from fastdiff._base import compare as compare_base
from fastdiff._native import compare as compare_native, initiate_instance


def test_content():
    """Sample pytest test function with the pytest fixture as an argument."""
    compared = compare("one\ntwo\nthree", "one\ntwo\nfour")
    assert compared == ['  one', '  two', '- three', '+ four']


CONTENTS1 = "one\ntwo\nthree\n"*100
CONTENTS2 = "one\ntwo\nfour\n"*100


def test_benchmark_content_base(benchmark):
    """Sample pytest test function with the pytest fixture as an argument."""
    def f():
        compare_base(CONTENTS1, CONTENTS2)
    benchmark(f)


def test_benchmark_content_native(benchmark):
    """Sample pytest test function with the pytest fixture as an argument."""
    def f():
        compare_native(CONTENTS1, CONTENTS2)
    
    benchmark(f)


def test_benchmark_compile_native(benchmark):
    """Sample pytest test function with the pytest fixture as an argument."""
    def f():
        initiate_instance()

    benchmark(f)
