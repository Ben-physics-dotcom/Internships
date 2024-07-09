import numpy as np

def chi_square(observed,expected,error):
  """
  observed:     That are the values that you observed.
  expected:     These values are the expected values. i.e. you get this through
                a linear regression
  error:        uncertainties of the observed values or the standard derivation
  """

  cs = np.sum((observed-expected)**2/error**2)
  return cs
