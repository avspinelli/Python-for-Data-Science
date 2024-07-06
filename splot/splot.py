import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


def splot(data, x, plot_type, y = None, y2 = None, recession = True,
          text = None, size = [11.326, 7] , golden_ratio = False, data_annotation = True,
          anot_stat = 'mean', bins = 10, reg = False, reg_order = 1, path = None, dpi = 400, custom_line = None, title = None):
    plt.close()
    
    if plot_type != 'distribution' and plot_type != 'scatterplot' and plot_type != 'lineplot' and plot_type != 'two lineplots' and plot_type != 'double lineplot':
        raise Exception( # Error exception for catching incorrect plot_types
            """
            Please use one of the following plot_type options:

            1. distribution
            2. scatterplot
            3. lineplot
            4. two lineplots
            5. double lineplot

            Basic structure is:

            splot(
                data = df,
                x = 'date',
                y = 'variable',
                plot_type = 'lineplot'
            )

            For more info: https://github.com/avspinelli/Python-Functions-for-Data-Science/tree/main/splot
            """
        )
    else:
        
        splot_palette = ["#27aeef", "#87bc45", "#ef9b20", "#b33dc6"] # HEX Codes to be used for colors
        
        
        #____ Recession function ____ https://fred.stlouisfed.org/series/USREC
        def recession_markers(alpha = .2, color = 'grey'):      # Generates economic recession markers on the plot for economic graphs, can be turned off with recession = False
            recession_df = [
                ['1902-10-1','1904-9-1'],['1907-6-1','1908-7-1'],['1910-2-1','1912-2-1'],['1913-2-1','1915-1-1'],
                ['1918-9-1','1919-4-1'],['1920-2-1','1921-8-1'],['1923-6-1','1924-8-1'],['1926-11-1','1927-12-1'],
                ['1929-9-1','1933-4-1'],['1937-6-1','1938-7-1'],['1945-3-1','1945-11-1'],['1948-12-1','1949-11-1'],
                ['1953-8-1','1954-6-1'],['1957-9-1','1958-5-1'],['1960-5-1','1961-3-1'],['1970-1-1','1970-12-1'],
                ['1973-12-1','1975-4-1'],['1980-2-1','1980-8-1'],['1981-8-1','1982-12-1'],['1990-8-1','1991-4-1'],
                ['2001-4-1','2001-12-1'],['2008-1-1','2009-7-1'],['2020-3-1','2020-5-1']
            ]
            
            for recession_periods in recession_df:   # After crteating the set of recessions, this applies them to a graph using plt.avxspan and a datetime object
                plt.axvspan(dt.datetime.strptime(recession_periods[0], '%Y-%m-%d'),
                            dt.datetime.strptime(recession_periods[1], '%Y-%m-%d'),
                            color=color, alpha=alpha, zorder = -1) 

        try:
            data[[x]].select_dtypes(include=[np.datetime64]).columns[0] # If the x var is not datetime, recession goes off
        except IndexError:
            recession = False
            
        if golden_ratio == False: # Golden ratio option to multiply any size[1] that you input by the golden ratio approximation of 1.618
            sns.set_theme(rc={'figure.figsize':(size[0],size[1])},style="ticks") # Set theme according to which size option you input
    
        
        elif golden_ratio == True:
            sns.set_theme(rc={'figure.figsize':(size[1] * 1.618, size[1])},style="ticks") # If Golden Ratio is true then shape to (x * 1.618)
    
    
        if plot_type == 'distribution': #____ Distribution ____ # https://seaborn.pydata.org/generated/seaborn.histplot.html
            recession = False           
            y = x                       # y = x for label formatting later on
            ax = sns.histplot(data[x], color = splot_palette[0], bins = bins, alpha = 1) # Do histplot
            if anot_stat == 'mean':
                ax.axvline(data[x].mean(), c='grey', ls='--', lw=2.5)                        # creates a grey mean on the distribution
            if anot_stat == 'median':
                ax.axvline(data[x].median(), c='grey', ls='--', lw=2.5)  # creates a grey median on the distribution

            if not custom_line == None:
                ax.axvline(custom_line, c=splot_palette[2], ls='--', lw=2.5)
                
            
            ax.yaxis.grid(color = 'grey', linestyle = 'dashed', alpha = .3, zorder = -1) # ax.yaxis.grid creates the background lines, in this case grey dashed lines
    
        elif plot_type == 'scatterplot': #____ Scatterplot ____ https://seaborn.pydata.org/generated/seaborn.scatterplot.html and https://seaborn.pydata.org/generated/seaborn.regplot.html
            recession = False
            
            if reg == True: # If the reg option is true, it will do a regplot instead of a simple scatterplot
                ax = sns.regplot(data = data, x = x, y = y, order=reg_order, color = splot_palette[0])     # If order is greater than 1, use numpy.polyfit to estimate a polynomial regression.
    
            elif reg == False: # else if its false it will default to a scatter plot
                ax = sns.scatterplot(data = data, x = x, y = y, color = splot_palette[0])
    
            ax.yaxis.grid(color = 'grey', linestyle = 'dashed', alpha = .3, zorder = -1)
            y2 = y    # This is for setting the title later on
            y = x
            
        else:
            # General data org
            # data[x] = data[x].astype('datetime64[ns]') # If plots are not a distribution or a scatterplot, assume the x is a date and apply datetime64[ns]
    
            g_start = data.sort_values(x, ascending = True).iloc[0][x] # Sets graphs start and end dates for time series data
            g_end = data.sort_values(x, ascending = False).iloc[0][x]
    
    
        if plot_type == 'lineplot': #____ Lineplot ____ https://seaborn.pydata.org/generated/seaborn.lineplot.html
    
            ax = sns.lineplot(x = x, y = y, data = data, color = splot_palette[0], alpha = 1)
    
    
        if plot_type == 'two lineplots': #____ plt.twinx() creates secondary y axis ____ https://seaborn.pydata.org/generated/seaborn.lineplot.html
    
    
            ax = sns.lineplot(x = x, y = y, data = data, color = splot_palette[0], alpha = 1)
            ax2 = plt.twinx()
            ax2 = sns.lineplot(x = x, y = y2, data = data, color = splot_palette[1], ax = ax2, alpha = 1) # ax = ax2 combines the two
            
            ax2.yaxis.grid(color = splot_palette[1], linestyle = 'dashed', alpha = .15) # Y label below bolds and puts a box around the label to identify line color
            ax2.set_ylabel(ax2.get_ylabel(), fontdict = {'weight': 'bold'}, bbox = dict(boxstyle = "square,pad=0.3", edgecolor = splot_palette[1], facecolor = "White"), rotation = -90, va='bottom')
    
    
        if plot_type == 'double lineplot': #____ similar to two lineplot except the lines are on the same axis ____ https://seaborn.pydata.org/generated/seaborn.lineplot.html
    
            
            data_melt = data.melt(id_vars = x, value_vars = [y,y2]) # pd.melt organizes the data for same axis plotting
            ax = sns.lineplot(x = x, y = 'value', data = data_melt, palette = splot_palette[:2], hue = 'variable', alpha = 1) 
            
            handles, labels = ax.get_legend_handles_labels() # Add legend
            ax.legend(handles=handles[:], labels=labels[:])
    
        
        # Standards - these are standard quality of life changes that each graph gets a combination of
        ax.set_xlabel(ax.get_xlabel(), fontdict = {'weight': 'bold'}) # create bold x label
        
        if recession == True: # If recession = True run the recession function established above
            recession_markers(alpha = .1) # made alpha adjustable for testing, or for others to change if they want darker recession bars
        if not title == None:
            ax.set_title(title)
        else:
            if plot_type == 'lineplot' or plot_type == 'distribution': # Depending on the plot they get a slightly diffrent title
                ax.set_title(f'{y} {plot_type.capitalize()}')
            else:
                ax.set_title(f'{y} : {y2}')
            
        if plot_type != 'distribution' and plot_type != 'scatterplot': # If not dist or scatter it is a time series which needs to be at within max and min dates
            ax.set(xlim=(g_start, g_end))
            ax.yaxis.grid(color = splot_palette[0], linestyle = 'dashed', alpha = .15)
    
        if plot_type == 'double lineplot': # double lineplot gets no y label because it gets a legend
            ax.set(ylabel='')
        if plot_type == 'scatterplot': # scatter gets just a bold y label, while others get a box around there
            ax.set_ylabel(ax.get_ylabel(), fontdict={'weight': 'bold'})
        else:
            ax.set_ylabel(ax.get_ylabel(), fontdict={'weight': 'bold'}, bbox = dict(boxstyle = "square,pad=0.3", edgecolor = splot_palette[0], facecolor = "White"))
    
    
        if data_annotation == True: # automatic mean or corr on the graph depending, very useful for variable selection when modeling
            
            if plot_type == 'lineplot' or plot_type == 'distribution':
    
                if anot_stat == 'mean':
                    metric_annotate = f'Mean: {round(data[y].mean(),3)}'
                if anot_stat == 'median':
                    metric_annotate = f'Median: {round(data[y].median(),3)}'

            else:
                metric_annotate = f'Corr: {round(data[[y,y2]].corr()[y][y2], 3)}'
                
            ax.annotate( # do annotation
                metric_annotate,
                xy=(-.08, 1.03),
                xycoords="axes fraction",
                bbox=dict(boxstyle="square,pad=0.3", edgecolor="grey", facecolor="White")
            )
    
        if text != None: # If you input an annotation it will put it on the graph, useful for notes or caveats
            
            ax.annotate(
                f'{text}',
                xy=(-.08, -0.13),
                xycoords="axes fraction",
                bbox=dict(boxstyle="square,pad=0.3", edgecolor="grey", facecolor="White")
            )
            
        plt.show() # show the plot
    
        if path != None: # save to path if you supply one
            
            fig = ax.get_figure()
            fig.savefig(path, dpi = dpi)
