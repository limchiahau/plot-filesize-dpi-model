# Modeling Plot Filesize

The purpose of this analysis is to create a linear model to predict the filesize of a matplotlib plot,
based on the dpi used in create the plot.

The analysis can be found at:

[Analysis](analysis.ipynb)

The linear model constructed is:

$\sqrt{\hat{filesize}} = 13.6108 + 0.3080 dpi$

The linear model shows that the square root of filesize increases by 0.3080 when dpi is increased by 1.