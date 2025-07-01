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
    data: dsjjhd

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
splot(data= df, x = 'Rental_Vacancy_Rate', plot_type = 'distribution', bins = 30,)
```
![alt text](https://github.com/avspinelli/Python-for-Data-Science/blob/main/splot/images/RVR_dist.png?raw=true)


