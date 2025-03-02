# Internships

In this repo are my data and Python Notebooks (NBs) from the internships during my Bachelor of Science at the Humboldt University at Berlin. It has the data and the analysis of the data.

## Some Statistical comments to the Notebooks

The two important statistical parameters in the NBs are the $R^2$ and the $\chi^2$. The only usecase for the $R^2$ are linear regressions. For linear regressions good choice can be `statsmodels.api`, because it gives multiple statistical parameter back. 
I used the following definition of the $\chi^2$ (Andrae, R., Schulze-Hartung, T., & Melchior, P. (2010). Dos and don'ts of reduced chi-squared. arXiv preprint arXiv:1012.3754.):

$$ \chi^2 = \frac{1}{n-p} \cdot \sum_i^n \frac{(observation_i-expected_i)^2}{\sigma^2_i} $$

The $\sigma^2$ can be the variance or can be the error value of the observation. The error of the observation can be calculated by gaussian error calculation:

$$ \sigma_i = \sqrt{\sum_{i=1}^m ( \partial_{x_i}f(x_1,x_2,...,x_m) \cdot u_{x_i})^2} $$

### How the plots are saved in the Notebooks

`plt.savefig('filename.png',dpi=600,transparent=True,bbox_inches='tight')`: You should name your plot with a specific name, so if you read the filename you know which plot it is. With the `dpi` you choose the resolution of your saved plot. With transparent equal to `True` you make your plot transparent. That feature is great, if you would make a presentation you can see the background through your plot. The `bbox_inches='tight'` is for the case that the axes labels or the legend would not be cut during the saving function of `matplotlib`.

## GPR 1

GPR stands for Grundpraktikum. Here I had the experiments F4, M2, M3, M5, M10, M12, T1 and T7. M stands for mechanics and T stands for thermodynamics.

## GPR 2

GPR stands for Grundpraktikum. This internship has two parts: the electrodynamics (ED) part and the optics part. Each part has his own folder (E_Experiments, Optics_Experiments). The ED folder has data and the notebooks for the following experiments: E1, E3, E4, E5 and E12. The data are available. 

## Information about the FPR-1

FPR stands for fortgeschrittenen Praktikum. It is important that you chance all sdt files into asc files, because in VS Code can read asc files, but not sdt files. If you want to change anything about your data, you could copy the data and put it from the asc file into a text file (.txt) or into a csv file.

## User information for running the notebooks

If you want to run my notebooks on a local computer please check before that you have installed MikTex or another TeX distribution on your local computer, because the axis titles need the TeX distribution.
