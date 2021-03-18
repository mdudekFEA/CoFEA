#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('import', 'numpy as np')
get_ipython().run_line_magic('import', 'pyvista as pv')
get_ipython().run_line_magic('from', 'ipywidgets import FloatSlider, FloatRangeSlider, Dropdown, Select, Box, AppLayout, jslink, Layout, VBox, HBox')
get_ipython().run_line_magic('from', 'ipygany import Scene, IsoColor, TetraMesh, Component, ColorBar, colormaps')



get_ipython().run_line_magic('mesh', "= TetraMesh.from_vtk('benchmarks/005-hemispherical-shell-point-load/hemisperical-shell-points-load.vtu', %show_edges = True)")

get_ipython().run_line_magic('u_min', '= 4.4e-6')
get_ipython().run_line_magic('u_max', '= 1.8e-1')

  # Colorize by height
get_ipython().run_line_magic('colored_mesh', "= IsoColor(mesh, input=('u','X1'), min=u_min, max=u_max)")

  # Create a slider that will dynamically change the boundaries of the colormap
get_ipython().run_line_magic('colormap_slider_range', '= FloatRangeSlider(value=[u_min, u_max], min=u_min, max=u_max, step=(u_max - u_min) / 100.)')

get_ipython().run_line_magic('jslink', "((colored_mesh, 'range'), (colormap_slider_range, 'value'))")

  # Create a colorbar widget
get_ipython().run_line_magic('colorbar', '= ColorBar(colored_mesh)')

  # Colormap choice widget
get_ipython().run_line_magic('colormap', '= Dropdown(')
get_ipython().run_line_magic('options', '=colormaps,')
get_ipython().run_line_magic('description', "='colormap:'")
get_ipython().run_line_magic(')', '')

get_ipython().run_line_magic('jslink', "((colored_mesh, 'colormap'), (colormap, 'index'))")

get_ipython().run_line_magic('AppLayout', '(')
get_ipython().run_line_magic('header', '=Scene([colored_mesh]),')
get_ipython().run_line_magic('left_sidebar', '=VBox((colormap, colormap_slider_range)),')
get_ipython().run_line_magic('right_sidebar', '=(colorbar),')
get_ipython().run_line_magic('pane_widths', '=[1, 0, 1],')
get_ipython().run_line_magic('pane_heights', "=['80','20',0],")
get_ipython().run_line_magic('footer', '=None,')
get_ipython().run_line_magic(')', '')

