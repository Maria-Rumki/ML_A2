"""
This type stub file was generated by pyright.
"""

from traitlets.config.configurable import Configurable

"""
A context manager for managing things injected into :mod:`builtins`.
"""
class __BuiltinUndefined:
    ...


BuiltinUndefined = ...
class __HideBuiltin:
    ...


HideBuiltin = ...
class BuiltinTrap(Configurable):
    shell = ...
    def __init__(self, shell=...) -> None:
        ...
    
    def __enter__(self): # -> Self@BuiltinTrap:
        ...
    
    def __exit__(self, type, value, traceback):
        ...
    
    def add_builtin(self, key, value): # -> None:
        """Add a builtin and save the original."""
        ...
    
    def remove_builtin(self, key, orig): # -> None:
        """Remove an added builtin and re-set the original."""
        ...
    
    def activate(self): # -> None:
        """Store ipython references in the __builtin__ namespace."""
        ...
    
    def deactivate(self): # -> None:
        """Remove any builtins which might have been added by add_builtins, or
        restore overwritten ones to their previous values."""
        ...
    

