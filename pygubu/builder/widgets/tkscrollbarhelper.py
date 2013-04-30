import tkinter as tk

from pygubu.builder.builderobject import *
from pygubu.widgets.tkscrollbarhelper import TkScrollbarHelper


class TKSBHelperBO(BuilderObject):
    class_ = TkScrollbarHelper
    container = False
    maxchildren = 1
    allowed_children = ('tk.Entry', 'ttk.Entry', 'tk.Text', 'tk.Canvas',
        'tk.Listbox', 'ttk.Treeview' )
    properties = ['scrolltype', 'borderwidth', 'cursor', 'height',
        'highlightbackground', 'highlightcolor', 'highlightthickness',
        'padx', 'pady', 'relief', 'takefocus', 'width']
    ro_properties = ('scrolltype', )

    def add_child(self, bobject):
        cwidget = bobject.widget
        self.widget.add_child(cwidget)


__scrolltype_property = {
    'input_method': 'choice',
    'values': (TkScrollbarHelper.BOTH, TkScrollbarHelper.VERTICAL,
        TkScrollbarHelper.HORIZONTAL),
    'default': TkScrollbarHelper.HORIZONTAL }

if 'scrolltype' not in CUSTOM_PROPERTIES:
    register_property('scrolltype', __scrolltype_property)


register_widget('pygubu.builder.widgets.tkscrollbarhelper', TKSBHelperBO,
    'ScrollbarHelper', ('Pygubu Helpers', 'tk'))
