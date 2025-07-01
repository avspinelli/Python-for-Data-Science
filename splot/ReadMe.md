# splot
### A quick and easy graphing function

Splot is an all in one graphing function which allows for easy graph creation / alteration. The function can create scatterplots, lineplots, distributions, barplots and box plots, with functionality to change colors, titles, recession bars, annotations, exporting, and more.

```ruby
splot(data, x, plot_type, y=None, recession=True, seperate_y_axis=False, text=None, size=[11.326, 7],
    golden_ratio=False, data_annotation=True, anot_stat='mean', bins=10, reg=False, reg_order=1, path=None, dpi=400,
    custom_line=None, custom_line2=None, title=None, bar_order=None, end_date=None,
    y_alpha=[1, 1, 1, 1, 1, 1, 1, 1, 1], splot_palette=['#27aeef', '#87bc45', '#ef9b20', '#b33dc6', '#E14636', '#E0C700'],
)
```

## Parameters:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **data :** ***pd.DataFrame***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Input data

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **x :** ***str***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Column to plot on the x axis

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **plot_type :** ***str***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Type of plot: distribution, scatterplot, lineplot, barplot, boxplot

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **y :** ***str, list, default None***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Column to plot on the y axis. Can be list: ['var1', 'var2']

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **recession :** ***bool, default True***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Adds recession markers for time series data

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **seperate_y_axis :** ***bool, default False***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; For lineplot with 2 y variables, will sepwrate y axis

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **text :** ***str, default None***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Text to be displayed as a footnote at the bottom of the plot

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **size :** ***list, default [11.326, 7]***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Image size

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **golden_ratio :** ***Bool, default False***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Snaps image size to the golden ratio: size[1] * 1.618

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **data_annotation :** ***Bool, default True***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Descriptive data annotation that changes per plot. For scatterplot, defaults to correlation, for other plots defaults to mean

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **anot_stat :** ***str, default mean***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Change the annotation stat to median for some plots

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **bins :** ***int, default 10***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Number of bins for distribution plot

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **reg :** ***Bool, default False***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Add a regression line to scatterplot

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **reg_order :** ***int, default 1***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; If order is greater than 1, use numpy.polyfit to estimate a polynomial regression

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **path :** ***str, default None***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Path for output png

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **dpi :** ***int, default 300***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; DPI for png output

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **custom_line :** ***float, datetime object, default None***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Creates a custom line on the x axis of the plot. Can be datetime object

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **custom_line2 :** ***float, datetime object, default None***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Creates a custom line on the x axis of the plot. Can be datetime object

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **title :** ***str, default None***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Customize title of plot

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **bar_order :** ***list, default None***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Specify the order of a barplot

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **end_date :** ***str, datetime, default None***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Custom end date of lineplot

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **y_alpha :** ***list, int, default [1,1,...]***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Set custom alpha for y variables in lineplot

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **splot_palette :** ***list, str, default ['#27aeef', '#87bc45', '#ef9b20', '#b33dc6', '#E14636', '#E0C700']***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Default color palette, can be altered for custom colors



## Quick Start


Quick Lineplot with recession markers, and some other fancy features (They can all be turned off, on by default):
```ruby
splot(data = df, x = 'period', y = 'Rental_Vacancy_Rate', plot_type = 'lineplot')
```
![alt text](https://github.com/avspinelli/Python-for-Data-Science/blob/main/splot/images/RVR.png?raw=true)

Adding a second line:
```ruby
splot(data= df, x = 'period', y = ['Rental_Vacancy_Rate','r15'], plot_type = 'lineplot', path = 'your/path/here/image.png')
```
![alt text](https://github.com/avspinelli/Python-for-Data-Science/blob/main/splot/images/RVR_R15.png?raw=true)

Two lineplots, one on each axis:
```ruby
splot(data= df, x = 'period', y = ['Rental_Vacancy_Rate','Homeownership_Rate'], plot_type = 'lineplot',seperate_y_axis = True, data_annotation = False)
```
![alt text](https://github.com/avspinelli/Python-for-Data-Science/blob/main/splot/images/RVR_HR2.png?raw=true)

Distributions:
```ruby
splot(data= df, x = 'Rental_Vacancy_Rate', plot_type = 'distribution', bins = 30)
```
![alt text](https://github.com/avspinelli/Python-for-Data-Science/blob/main/splot/images/RVR_dist.png?raw=true)


