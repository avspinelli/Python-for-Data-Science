# splot
### A quick and easy graphing function

Splot is an all in one graphing function which allows for easy graph creation / alteration. The function can create scatterplots, lineplots, distributions, barplots and box plots, with functionality to change colors, titles, recession bars, annotations, exporting, and more.

## Quick Start


#### Quick Lineplot with recession markers, and some other fancy features
```ruby
splot(data = df, x = 'period', y = 'Rental_Vacancy_Rate', plot_type = 'lineplot')
```
![alt text](https://github.com/avspinelli/Python-for-Data-Science/blob/main/splot/images/RVR.png?raw=true)

#### Adding a second line
```ruby
splot(data= df, x = 'period', y = ['Rental_Vacancy_Rate','r15'], plot_type = 'lineplot', path = 'your/path/here/image.png')
```
![alt text](https://github.com/avspinelli/Python-for-Data-Science/blob/main/splot/images/RVR_R15.png?raw=true)



