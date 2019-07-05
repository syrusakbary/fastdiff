# -*- coding: utf-8 -*-

"""Main module."""

try:
    from ._native import compare
except:
    # If any errors happen, fall back to the base approach
    from ._base import compare

__all__ = ["compare"]
