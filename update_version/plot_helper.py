#!/usr/bin/env python
# coding: utf-8

# In[11]:


from matplotlib import pyplot

class MyPlot: 
    
    
    """MyPlot is a parent class for Trend and Fluctuations child classes.
    In MyPlot are store all the shared private methods and the inizialization
    attributes"""
    
    def __init__(self, df, data: list):
        self.df = df
        self.data = data
        self.plt = pyplot
    
    def _make_a_line(self, ax, fig):
        
        "Private method that plot a red line above the graph."
        
        ax.plot([0.12, .9],          # Set width of line
        [1.05, 1.05],                # Set height of line
        transform=fig.transFigure,   # Set location relative to plot
        clip_on=False, 
        color='#E3120B', 
        linewidth=.6)
    
    def _make_a_rec(self, ax, fig):
        
        "Private method that plots a red rectangle above on the top right corner."
        
        ax.add_patch(self.plt.Rectangle((0.12,1.05),        # Set location of rectangle by lower left corder
                           0.04,                       # Width of rectangle
                           -0.02,                      # Height of rectangle. Negative so it goes down.
                           facecolor='#E3120B', 
                           transform=fig.transFigure, 
                           clip_on=False, 
                           linewidth = 0))
    
    def _add_title(self, title, ax, fig):
        
        "Private method that adds a title."
        
        ax.text(x=0.12, y=0.98, s=title, 
            transform=fig.transFigure, ha='left', 
            fontsize=13, weight='bold', alpha=.8)
    
    def _add_description(self, description, ax, fig):
        
        "Private method that adds a description/subtitle if passed."
        ax.text(x=0.12, y=0.93, s=description, 
            transform=fig.transFigure, ha='left', 
            fontsize=11, alpha=.8)
        
            
    

class Trend(MyPlot):
        
    """Children class of MyPlot. Used to plot graphs represnting the trend of one
    or more variables."""
    
    def plot(self, title: str, description = ""):
        
        #creating fig and ax as attributes of the objects allows us to modify
        #other aspects of the graph more easily
        self.fig, self.ax = self.plt.subplots()
        
        for col in self.data:  
            #the for loop is needed because we may want to plot more than one variable
            self.ax.plot('Date', col, data = self.df)
        
        self._make_a_line(self.ax, self.fig)
        self._make_a_rec(self.ax, self.fig)
        
        self._add_title(title, self.ax, self.fig)
        
        if description != "":
            self._add_description(description, self.ax, self.fig)
        
    
    
    
    
class Fluctuations(MyPlot):
    
    """"Children class of MyPlot. Used to plot graphs representing the fluctuation of a
    series from some derived trend."""
    
    def __init__(self, df, data: str, trend: list): #we need to add the object attribute trend which was not need in Trend
        super().__init__(df, data)
        self.trend = trend
    
    def plot(self, title, description = ""):
        
        self.fig, self.ax = self.plt.subplots()
        
        for tr in self.trend:
            fluctuations = self.df[self.data] - tr
            self.ax.plot(df.Date, fluctuations)
        
        self._make_a_line(self.ax, self.fig)
        self._make_a_rec(self.ax, self.fig)
        
        self._add_title(title, self.ax, self.fig)
        
        if description != "":
            self._add_description(description, self.ax, self.fig)
        
        

