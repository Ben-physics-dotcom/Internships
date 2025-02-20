# Importe
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import sympy as sym
from scipy.stats import chisquare
from scipy.stats import gaussian_kde

#Messwerte:

V12_f = np.array([737.2, 757.31, 785.40, 800.27, 829.89, 894.56, 988.51, 1200.7, 1364.8, 1444.7, 1549.2, 1657.4, 1809.8, 1937.9, 737.9, 730.38, 720.56, 717.34, 708.42, 700.71, 689.33, 656.61, 614.34, 557.66, 509.05, 481.46, 400.77, 143.68, 100.27]) #frequenz in Hz

V12_USSI = np.full_like(V12_f, 15) #SSSpannung in V

V12_USSII = np.array([0.45, 0.37, 0.3, 0.26, 0.21, 0.15, 0.1, 0.07, 0.05, 0.04, 0.04, 0.04, 0.03, 0.03, 0.4, 0.4, 0.4, 0.39, 0.37, 0.34, 0.3, 0.22, 0.16, 0.11, 0.09, 0.08, 0.07, 0.02, 0.01])

#Unsicherheiten:

V12_U_USSI = np.full_like(V12_f,0.5)
V12_U_USSII = np.full_like(V12_f,0.0005)

# Fit
#29er Arrays erstellen
R_P_29 = np.full_like(V12_f, R_P)

U_R_P_29 = np.full_like(V12_f, U_R_P)

L_29 = np.full_like(V12_f, V4_L)

C_29 = np.full_like(V12_f, V3_C)

#Komplexer Wds
V12_Z = R_P_29 * (V12_USSI - V12_USSII) / V12_USSII

#Unsicherheit
V12_U_Z = np.sqrt(((V12_USSI - V12_USSII) / V12_USSII * U_R_P_29)**2 + (R_P_29 / V12_USSII * V12_U_USSI)**2 + (R_P_29 * V12_USSI / (V12_USSII**2) * V12_U_USSII)**2)

# Zur ermittlung des Fits wurden die Parameter nacheinander ermittelt
#L festlegen
V12_Z_fit_1 = lambda x, a: np.sqrt((a * x)**2  + (1/(V3_C*np.pi*2 * x))**2 - 2*a/(V3_C*np.pi*2) + R_SP**2)
g11, g11Cov = optimize.curve_fit(V12_Z_fit_1, V12_f, V12_Z, sigma=V12_U_Z)

V12_L = g11[0]/(2 * np.pi)
V12_U_L = np.sqrt(g11Cov[0][0])/ (2* np.pi)
print("Induktivität: ", V12_L, "+-", V12_U_L, "H")

#C festlegen
V12_Z_fit_2 = lambda x, a: np.sqrt((g11[0] * x)**2  + (1/(a * x))**2 - 2*g11[0]/a + R_SP**2)
g12,g12Cov = optimize.curve_fit(V12_Z_fit_2, V12_f, V12_Z, sigma=V12_U_Z)

V12_C = g12[0]/(2 * np.pi)
V12_U_C = np.sqrt(g12Cov[0][0])/(2 * np.pi)
print("Kapazität : ", V12_C, "+-", V12_U_C)

#R und übrige Param festlegen
V12_Z_fit_3 = lambda x, b, d, e: np.sqrt((g11[0] *x + b - 1/(g12[0] *x + d))**2 + e**2)
g13,g13Cov = optimize.curve_fit(V12_Z_fit_3, V12_f, V12_Z, sigma=V12_U_Z)

V12_RSP = g13[2]
V12_U_RSP = np.sqrt(g13Cov[2][2])
print("Spulenwds: ", V12_RSP, "+-", V12_U_RSP)
print("a :", g11[0], "+-", np.sqrt(g11Cov[0][0]))
print("b :", g13[0], "+-", np.sqrt(g13Cov[0][0]))
print("c :", g12[0], "+-", np.sqrt(g12Cov[0][0]))
print("d :", g13[1], "+-", np.sqrt(g13Cov[1][1]))
print("e :", g13[2], "+-", np.sqrt(g13Cov[2][2]))

V12_Z_fit = lambda x, a, b, c, d, e : np.sqrt((a * x + b - 1/(c *x + d))**2 + e**2)

plt.plot(V12_f, V12_Z, "bo")
plt.plot(np.arange(60, 2001, 10), V12_Z_fit(np.arange(60, 2001, 10), g11[0], g13[0], g12[0], g13[1], g13[2]))
plt.errorbar(V12_f, V12_Z, yerr=V12_U_Z, fmt=".")
plt.legend(("Messwerte", "Fit |Z(f)|"))
plt.xlabel("Frequenz in Hz")
plt.ylabel("Scheinwiderstand in Ohm")

# chi^2
chisquare( V12_Z_fit(V12_f, g11[0], g13[0], g12[0], g13[1], g13[2]),V12_Z)


# Resdiuen
plt.figure(figsize=(6.4, 2))
plt.plot(V12_f, V12_Z-V12_Z_fit(V12_f, g11[0], g13[0], g12[0], g13[1], g13[2]), "bo")
plt.axhline(y=0)
plt.ylabel("Residuen")
plt.xlabel("Frequenz in Hz")
