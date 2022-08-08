import sys

class _bdconst:
    class ConstError(PermissionError):
        """
        Modify exception
        """
        pass
    
    class ConstCaseError(ConstError):
        """
        Case exception
        """
        pass
    
    def __setattr__(self, name: str, value):
        """
        Constant setting
        """
        if name in self.__dict__:
            raise self.ConstError("Can't change const {0}".format(name))
        
        if not name.isupper():
            raise self.ConstCaseError("Const name {0} is not all uppercase".format(name))
        
        self.__dict__[name] = value
    
    def __delattr__(self, name: str):
        """
        Constant deletion
        """
        pass
    
    def __getattr__(self, name):
        """
        Returns None for non-existent constants
        """
        return None

# Add constant instance to system module
sys.modules['bdpyconst'] = _bdconst()