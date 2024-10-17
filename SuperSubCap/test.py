from __init__ import maping
import re
def smart_morph(arg:str,style:str=""):
    """
    take arg (str) and transforms it using nicer notation (Latex or Python by default)
    Specify style to change the output format (Python, Latex, ""[for both])
    
    Latex syntax to standart text using superscript and subscript, as well as greek letters
    """
    
    if style == "Latex":
        """
        Latex style
        Includes _ as subscript and ^ as superscript
        Checks for {} too
        Transforms greek letters too
        """
        single_or_long_re = r"((?:{[^{}]*})|[^_\s])" #gm #global multiline
        # (?:{[^{}]*}) # this is the group that is matched if it is a long string
        # {[^{}]*} # this is the long string
        # [^_\s] # this is the group that is matched if it is a single character
        
        # replace the superscript
        res1 = re.sub(r"\^"+single_or_long_re,lambda m:print(m),arg)
        return res1

#actually it's hard to work with regex I give up for now...

print(smart_morph(r"ab^31_54_54c^{5\alpha/2,3!}","Latex"))