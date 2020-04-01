#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pathlib
import pandas as pd
import functools


# In[ ]:


class Model:
    root_dir = pathlib.Path('plots')
    
    def __init__(self):
        num_points = [100,1000,10000]
        self._data_dir = [self.root_dir / str(points) for points in num_points]
    
    @property
    def data(self):
        def join_df(first, second):
            return first.append(second, ignore_index=True)
        
        data_df = [self._to_df(folder) for folder in self._data_dir]
        return functools.reduce(join_df, data_df)
    
    def _to_df(self,folder):
        '''Takes a Path object returns a dataframe.
        
        The columns of the dataframe are:
        1) dpi
        2) filesize
        3) num_points
        '''
        plots = {self._plot_stats(plot) for plot in folder.iterdir()}
        result_df = pd.DataFrame(plots, columns=['dpi', 'filesize'])
        
        num_points = self._num_points(folder)
        result_df = result_df.assign(num_points=num_points)
        return result_df
    
    def _plot_stats(self,file):
        '''returns a tuple where the first value
        represents dpi and the second value represents filesize.
        
        The dpi is the name of the file without the extension.
        '''
        dpi = int(file.stem)
        filesize = file.stat().st_size
        
        return (dpi, filesize)
    
    def _num_points(self,folder):
        return int(folder.stem)

