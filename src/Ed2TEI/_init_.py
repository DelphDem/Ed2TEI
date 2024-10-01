# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:40:53 2024

@author: DelphDem
"""

from .process_text import create_tei
from .add_variants import add_variants
from .add_rejected import add_rejected
from .add_notes import add_notes

__all__ = ['create_tei', 'add_variants', 'add_rejected', 'add_notes']