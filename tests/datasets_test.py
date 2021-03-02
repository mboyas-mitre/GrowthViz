import pytest

from growthviz.datasets import read_percentiles

def test_read_percentiles():
  p = read_percentiles('bmiagerev.csv')
  assert (p['P50'] == p['M']).all()