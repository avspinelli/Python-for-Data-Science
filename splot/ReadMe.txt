splot
splot(data, x, y = None, plot_type, y2 = None, recession = True, text = None, size = [11.326, 7] , golden_ratio = False, data_annotation = True, bins = 10, reg = False, reg_order = 1, path = None)

Creates graphs with economic modelingn in mind. Has the ability to produce multiple kinds of graphs, add recession indicator bars, annotate with text, export graphs to a path, and more.


Parameters:

Data: pands.DataFrame
    input data frame containing your x and y variables (or x, y and y2 for multiple y's). Assumes y is a numeric type, while x can be numeric or datetime. if datetime you can use the recession function, if not it will disable

x, y, y2: string
    will be your column name for each type - ie x = 'period', y = 'rent', y2 = 'vacancy'

plot_type: string: 'distribution', 'lineplot', 'two lineplots', 'double lineplot', 'scatterplot'
    
    distrobution: requires just x. basic distrobution plot. has the option bins to change the density of bins. see https://seaborn.pydata.org/generated/seaborn.histplot.html
    
    lineplot: requires just x and y. simple lineplot. see https://seaborn.pydata.org/generated/seaborn.lineplot.html
    
    two lineplots: requires y and y2. two lines on one graph on two diffrent y axis. most useful for comparing variables that dont measure the same things (like inflation and the unemployment rate). Uses the plt.twinx() method. see https://seaborn.pydata.org/generated/seaborn.lineplot.html
    
    double lineplot: requires y and y2. two lines on one graph on the same axis. Great for comparing two similar variables that use the same or similar type of measurement. uses the pd.melt and sns hue method. see https://seaborn.pydata.org/generated/seaborn.lineplot.html
    
    scatterplot: requires y and y2. creates a scatterplot. if the reg option equals True, it will create a regplot, which uses ols to plot a line of best fit over the scatter plot, as well as a confidence interval. If order is greater than 1, use numpy.polyfit to estimate a polynomial regression. see https://seaborn.pydata.org/generated/seaborn.scatterplot.html and https://seaborn.pydata.org/generated/seaborn.regplot.html

recession: boolean
    if True, it adds recession markers which are taken directly from NBER definitions here https://fred.stlouisfed.org/series/USREC. x must be datetime for it to work. if x is numeric it wil default to false

text: string
    adds text to the bottom of the graph

size: (width, height)
    sets the size of the graph in inches

golden_ratio: boolean
    if True, the given height will be multipliued by the golden ratio approx of 1.618 to get the width, no matter the given width

data_annotation: boolean
    for distributions and lineplots it will display the variables mean in the upper left. for double lineplot, two lineplots, and scatterplot it will display the correlation

bins: int
    used with the distribution option. plots to set the number of bins used

reg: boolean
    used with the scatterplot option. if true, will use the seaborn.regplot option, which plots an old line of best fit and confidence interval

reg_order: int
    used with the scatterplot option. If order is greater than 1, use numpy.polyfit to estimate a polynomial regression

path: string
    export path




