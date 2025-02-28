import numpy as np
import statsmodels.api as sm


def lin_reg(x, a, b):
    y = a * x + b
    return y


def chi_sq(y, fx, u_y, p=2):    # für 2 Fitparameter
    """
    Variables
      n [int]:                length of the
      y [numpy array]:        y values for the y axis
      fx [numpy array]:       y values from the regression
      u_y[int, numpy array]:  Unsicherheit/uncertainty from y
      p [int]:                number of parameters of the regression
    Return:
      chi square
    """
    n = len(y)
    factor = 1 / (n - p)
    return factor * np.sum((y - fx)**2 / u_y**2)


def reg_wls(x, y, uy, a_round=3, b_round=3, r_round=4):
    '''
    Variables:
      x [numpy array, pandas serie]: x-data
      y [numpy array, pandas serie]:
      uy [int, numpy array, pandas serie]: uncertainties/standard derivation of y
      a_round [int]: number of digits after the point (us) or comma (german)
      b_round [int]: number of digits after the point (us) or comma (german)
      r_round [int]: number of digits after the point (us) or comma (german)

    Returning variables:
      a:    from a*x+b
      ua:   uncertainty of a
      b:    from a*x+b
      ub:   uncertainty of b
      R:    R square
      chi:  chi square
    '''
    # calculating regression
    X = sm.add_constant(x)
    model = sm.WLS(y, X, weights=uy)
    results = model.fit()
    print(results.summary())

    # Parameters
    a = round(results.params[1], a_round)
    b = round(results.params[0], b_round)
    ua = round(results.bse[1], a_round)
    ub = round(results.bse[0], b_round)
    R = round(results.rsquared, r_round)
    residuals = np.array(results.resid)

    # lin. Reg.
    f_x = a * x + b

    # chi square
    chi = round(chi_sq(x, y, f_x, uy), 3)

    return a, ua, b, ub, R, chi, residuals


def reg_ols(x, y, a_round=3, b_round=3, r_round=4):
    '''
    Variables:
      x [numpy array, pandas serie]: x-data
      y [numpy array, pandas serie]:
      a_round [int]: number of digits after the point (us) or comma (german)
      b_round [int]: number of digits after the point (us) or comma (german)
      r_round [int]: number of digits after the point (us) or comma (german)

    Returning variables:
      a:    from a*x+b
      ua:   uncertainty of a
      b:    from a*x+b
      ub:   uncertainty of b
      R:    R square
    '''
    # calculating regression
    X = sm.add_constant(x)
    model = sm.OLS(y, X)
    results = model.fit()
    print(results.summary())

    # Parameters
    a = round(results.params[1], a_round)
    b = round(results.params[0], b_round)
    ua = round(results.bse[1], a_round)
    ub = round(results.bse[0], b_round)
    R = round(results.rsquared, r_round)
    residuals = np.array(results.resid)

    return a, ua, b, ub, R, residuals
