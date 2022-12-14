# Version 0.0.3
# Help displays cleaned up and lib tested
# Added sub <-> super translation
# Added caps <-> smalls and help improved

SUMMARY = """%s, library to switch between normal, superscripts, subscripts and caps.
Including greek letters, numbers and basic operands
%s.info() for more info"""%(__name__,__name__)

# For small info
__doc__ = SUMMARY
# help(module_name) or info(module_name) for more infos

alls = ["%s"%(__name__),
        "SUMMARY",
        "alls",
        "help_letters",
        "greek_letters",
        "greek_letters_to_latin",
        "superscripts",
        "superscripts_to_normal",
        "subscripts",
        "subscripts_to_normal",
        "subscripts_to_superscripts",
        "superscripts_to_subscripts",
        "small_to_caps",
        "caps_to_small",
        "maping"]
# 15 elements

# Really detailled informations
def info(*targets:str):
    """info() : get general info about this library
    info(param) : get detailled informations about param
    Parameters: str ==> info about str
    """
    help_letters = {# Content of this library
                    # Library general info
                    "%s"%(__name__):"""Help on module %s:

    %s has %s elements to switch between different letters types:
    Between small and caps, normal to subscripts or superscripts and opposites.
    All letters include latin small and caps and greek small and caps.
    Superscripts and subscripts include numbers and operands.
    info(elem) for more info on elem in %s.alls"""%( __name__, __name__, len(alls)-4,__name__),
                    # SUMMARY
                    "SUMMARY":"""Help on SUMMARY in module %s:

    SUMMARY: summary of this library
    Content of library : alls (list)
    help for all contents of library : help_letters (dict)"""%(__name__),

                    # alls
                    "alls":"""Help on alls in module %s:

    alls: alls[0:3] --> lib info object
    alls: alls[4:14] --> dict name
    lib info object discribing the contents of this library
    dict name in this file discribing a translation between letter types
    alls: alls[14:%s] --> helpful functions"""%(__name__,len(alls)),
                    
                    # help_letters
                    "help_letters":"""Help on help_letters in module %s:

    help_letters: help_letters[dict] --> documentation for dict
    with dict name contained in alls (list type) 
    Documentation for these dicts for letters - subscripts-superscripts translations"""%(__name__),
                    
                
                # greek_letters
                    "greek_letters":"""Help on greek_letters in module %s:

    greek_letters : latin --> greek
        - Smalls latin
        - Capitals latin
    Ref key latin to greek from https://bailly.app/
    small and capps and var{letter} for variation style
    Feedback to the dev is welcomed"""%(__name__),
                    
                    "greek_letters_to_latin":"""Help on greek_letters_to_latin in module %s:

    greek_letters_to_latin : greek --> latin
        - Smalls greek
        - Capitals greek
    Ref key greek to latin from https://bailly.app/ 
    small and capps available
    Feedback to the dev is welcomed"""%(__name__),
                
                
                # Superscripts
                    "superscripts":"""Help on superscripts in module %s:

    superscripts : normal --> superscript equivalent
        - Numbers and operands
        - Smalls latin
        - Capitals latin
        - Smalls greek
        - Capital greek
    Not all letters have proper equivalent but best is given
    Feedback to the dev is welcomed"""%(__name__),
                    
                    "superscripts_to_normal":"""Help on superscripts_to_normal in module %s:

    superscripts_to_normal : superscript --> normal equivalent
        - Numbers and operands
        - Smalls latin
        - Capitals latin
        - Smalls greek
        - Capital greek
    Not all letters have superscripts equivalent
    so this conversion may not be accurate
    Feedback to the dev is welcomed"""%(__name__),
                
                
                # Subscripts
                    "subscripts":"""Help on subscripts in module %s:

    subscripts: normal --> subscripts equivalent
         - Numbers and operands
         - Smalls latin
         - Capitals latin
         - Smalls greek
         - Capital greek
     Not all letters have subscrips equivalent but best is given
     Feedback to the dev is welcomed"""%(__name__),
                    
                    "subscripts_to_normal":"""Help on subscripts_to_normal in module %s:

    subscripts_to_normal: subscript --> normal
         - Numbers and operands
         - Smalls latin
         - Capitals latin
         - Smalls greek
         - Capital greek
     Not all letters have subscripts equivalent so this conversion 
     may not be accurate
     Feedback to the dev is welcomed"""%(__name__),


                # Subscript to superscript
                "subscripts_to_superscripts":"""Help on subscripts_to_superscripts in module %s:
    subscripts_to_superscripts: subscript --> superscript equivalent
         - Numbers and operands
         - Smalls latin
         - Capitals latin
         - Smalls greek
         - Capital greek
    Not all subscripts have superscripts equivalent but the best is given
    use "var??" for alternate gamma input
    Feedback to the dev is welcomed"""%(__name__),


                # Superscript to subscript
                "superscripts_to_subscripts":"""Help for superscripts_to_subscripts in module %s:
    superscripts_to_subscripts: superscript --> subscript equivalent
         - Numbers and operands
         - Smalls latin
         - Capitals latin
         - Smalls greek
         - Capital greek
    Not all superscripts have subscripts equivalent but the best is given
    Feedback to the dev is welcomed"""%(__name__),
                # Smalls to caps
                "small_to_caps":"""Help for small_to_caps in module %s:
    small_to_caps : small --> caps equivalent
        - latin
        - Superscripts latin
        - Subscripts latin
        - greek
        - Superscripts greek
        - Subscripts greek
    Not all smalls gave caps equivalent, best is given.
    Feedback to the dev is welcomed"""%(__name__),
                # Caps to smalls 
                "caps_to_small":"""Help on caps_to_small in module %s:
    caps_to_small: caps --> small equivalent
        - Latin
        - Superscripts latin
        - Subscripts latin
        - Greek
        - Superscripts greek
        - Subscripts greek
    Not all caps have smalls equivalent, best if given.
    Feedback to the dev is welcomed"""%(__name__),


        # Functions
            # maping
            "maping":"""Help on maping in module %s:
    maping: str,format,default_fill --> transformed str in given format
    if the caracter is not available in end format, replace with default_fill
    checks if disabled increase perf but doesn't perform checks on inputs ==> less stable"""%(__name__)
                }
    if targets == tuple():
        print(help_letters["%s"%(__name__)])
    for target in targets:
        if target in alls:
            print(help_letters[target],end="\n\n")
        else:
            print(target,"not in",__name__,"module.")
    return None

greek_letters = {# Smalls latin
                 "a":"??","b":"??","varb":"??","c":"??","d":"??","e":"??","f":"??","varf":"??","g":"??",
                 "h":"??","i":"??","k":"??","l":"??","m":"??","n":"??","o":"??","p":"??","q":"??","varq":"??",
                 "r":"??","s":"??","vars":"??","t":"??","u":"??","v":"??","w":"??","x":"??","y":"??","z":"??",
                 # Capitals latin
                 "A":"??","B":"??","C":"??","D":"??","E":"??","F":"??","G":"??",
                 "H":"??","I":"??","K":"??","L":"??","M":"??","N":"??","O":"??","P":"??","Q":"??",
                 "R":"??","S":"??","T":"??","U":"??","V":"??","W":"??","X":"??","Y":"??","Z":"??"}

greek_letters_to_latin = {# Smalls greek
                          "??":"a","??":"b","??":"b","??":"c","??":"d","??":"e","??":"f","??":"f",
                          "??":"g","??":"h","??":"i","??":"k","??":"l","??":"m","??":"n","??":"o",
                          "??":"p","??":"q","??":"q","??":"r","??":"s","??":"s","??":"t",
                          "??":"u","??":"v","??":"w","??":"x","??":"y","??":"z",
                          # Capitals greek
                          "??":"A","??":"B","??":"C","??":"D","??":"E","??":"F","??":"G",
                          "??":"H","??":"I","??":"K","??":"L","??":"M","??":"N","??":"O",
                          "??":"P","??":"Q","??":"R","??":"S","??":"T","??":"U","??":"V",
                          "??":"W","??":"X","??":"Y","??":"Z",}

superscripts = {# Numbers and operands
              "0":"???","1":"??","2":"??","3":"??","4":"???","5":"???","6":"???","7":"???","8":"???","9":"???",
              "+":"???","-":"???","=":"???","(":"???",")":"???",
              # Smalls latin
              "a":"???","b":"???","c":"???","d":"???","e":"???","f":"???","g":"???","h":"???","i":"???","j":"??",
              "k":"???","l":"??","m":"???","n":"???","o":"???","p":"???","q":"???","r":"??","s":"??","t":"???",
              "u":"???","v":"???","w":"??","x":"??","y":"??","z":"???",
              # Capitals latin
              "A":"???","B":"???","C":"???","D":"???","E":"???","F":"???","G":"???","H":"???","I":"???","J":"???",
              "K":"???","L":"???","M":"???","N":"???","O":"???","P":"???","Q":"???","R":"???","S":"??","T":"???",
              "U":"???","V":"???","W":"???","X":"??","Y":"??","Z":"???",
              # Smalls greek
              "??":"???","??":"???","??":"???","??":"??","??":"???","??":"???","??":"???","??":"???","??":"??","var??":"???",
              "??":"??","??":"???","??":"???","??":"??","??":"??","??":"???","??":"???","??":"??","??":"??",
              "??":"??","??":"??","??":"??","??":"??","??":"??","??":"???","??":"??","??":"??","??":"???",
              "??":"??","??":"??",
              # Capital greek
              "??":"???","??":"???","??":"??","??":"???","??":"???","??":"???","??":"???",
              "??":"???","??":"???","??":"???","??":"^","??":"???","??":"???","??":"???","??":"??","??":"??",
              "??":"???","??":"??","??":"???","??":"??","??":"??","??":"??","??":"???","??":"??","??":"???",
              }

superscripts_to_normal = {# Numbers and operands
                          "???":"0","??":"1","??":"2","??":"3","???":"4","???":"5","???":"6","???":"7","???":"8","???":"9",
                          "???":"+","???":"-","???":"=","???":"(","???":")",
                          # Smalls latin
                          "???":"a","???":"b","???":"c","???":"d","???":"e","???":"f","???":"g",
                          "???":"h","???":"i","??":"j","???":"k","??":"l","???":"m","???":"n",
                          "???":"o","???":"p","???":"q","??":"r","??":"s","???":"t","???":"u",
                          "???":"v","??":"w","??":"x","??":"y","???":"z",
                          # Capitals latin
                          "???":"A","???":"B","???":"C","???":"D","???":"E","???":"F","???":"G",
                          "???":"H","???":"I","???":"J","???":"K","???":"L","???":"M","???":"N",
                          "???":"O","???":"P","???":"Q","???":"R","??":"S","???":"T","???":"U",
                          "???":"V","???":"W","??":"X","??":"Y","???":"Z",
                          # Smalls greek
                          "???":"??","???":"??","???":"??","??":"??","???":"??","???":"??","???":"??",
                          "???":"??","??":"??","???":"var??","??":"??","???":"??","???":"??","??":"??",
                          "??":"??","???":"??","???":"??","??":"??","??":"??","??":"??","??":"??",
                          "??":"??","??":"??","??":"??","???":"??","??":"??","??":"??","???":"??",
                          "??":"??","??":"??",
                          # Capital greek
                          "???":"??","???":"??","??":"??","???":"??","???":"??","???":"??","???":"??",
                          "???":"??","???":"??","???":"??","^":"??","???":"??","???":"??","???":"??",
                          "??":"??","??":"??","???":"??","??":"??","???":"??","??":"??","??":"??",
                          "??":"??","???":"??","??":"??","???":"??",}

subscripts = {# Numbers and operands
             "0":"???","1":"???","2":"???","3":"???","4":"???","5":"???","6":"???","7":"???","8":"???","9":"???",
             "+":"???","-":"???","=":"???","(":"???",")":"???",
             # Smalls latin
             "a":"a","b":"b","c":"c","d":"d","e":"???","f":"f","g":"g",
             "h":"???","i":"???","j":"???","k":"???","l":"???","m":"???","n":"???",
             "o":"???","p":"???","q":"q","r":"???","s":"???","t":"???","u":"???",
             "v":"???","w":"w","x":"???","y":"y","z":"z",
             # Capitals latin
             "A":"???","B":"???","C":"????" ,"D":"????" ,"E":"???","F":"????","G":"????",
             "H":"???","I":"???","J":"???","K":"???","L":"???","M":"???","N":"???",
             "O":"???","P":"???","Q":"???","R":"???","S":"???","T":"???","U":"???",
             "V":"???","W":"????","X":"???","Y":"???","Z":"????",
             # Smalls greek
             "??":"??","??":"???","??":"???","??":"??","??":"??","??":"??","??":"???","??":"???","??":"???","var??":"???", # here
             "??":"??","??":"??","??":"???","??":"??","??":"??","??":"???","??":"???","??":"??","??":"??","??":"??",
             "??":"???","??":"??","??":"??","??":"???","??":"???","??":"??","??":"??","??":"???","??":"??","??":"??",
             # Capital greek
             "??":"???","??":"???","??":"??","??":"??","??":"???","??":"???","??":"???",
             "??":"???","??":"???","??":"???","??":"??","??":"???","??":"???","??":"???","??":"??","??":"??",
             "??":"???","??":"??","??":"???","??":"???","??":"??","??":"??","??":"???","??":"??","??":"????",
             }

subscripts_to_normal = {# Numbers and operands
                        "???":"0","???":"1","???":"2","???":"3","???":"4","???":"5","???":"6","???":"7","???":"8","???":"9",
                        "???":"+","???":"-","???":"=","???":"(","???":")",
                        # Smalls latin
                        "a":"a","b":"b","c":"c","d":"d","???":"e","f":"f","g":"g",
                        "???":"h","???":"i","???":"j","???":"k","???":"l","???":"m","???":"n",
                        "???":"o","???":"p","q":"q","???":"r","???":"s","???":"t","???":"u",
                        "???":"v","w":"w","???":"x","y":"y","z":"z",
                        # Capitals latin (none exist, found replacements)
                        "???":"A","???":"B","????":"C" ,"????":"D","???":"E","????":"F","????":"G",
                        "???":"H","???":"I","???":"J","???":"K","???":"L","???":"M","???":"N",
                        "???":"O","???":"P","???":"Q","???":"R","???":"S","???":"T","???":"U",
                        "???":"V","????":"W" ,"???":"X","???":"Y","????":"Z",
                        # Smalls greek
                        "??":"??","???":"??","???":"??","??":"??","??":"??","??":"??","???":"??",
                        "???":"??","???":"??","??":"??","??":"??","???":"??","??":"??","??":"??","???":"??",
                        "???":"??","??":"??","??":"??","??":"??","???":"??","??":"??","??":"??",
                        "???":"??","???":"??","??":"??","??":"??","???":"??","??":"??","??":"??",
                        # Capitals Greek
                        "???":"??","???":"??","??":"??","??":"??","???":"??","???":"??","???":"??",
                        "???":"??","???":"??","???":"??","??":"??","???":"??","???":"??","???":"??",
                        "??":"??","??":"??","???":"??","??":"??","???":"??","???":"??","??":"??",
                        "??":"??","???":"??","??":"??","????":"??"}

subscripts_to_superscripts = {# Numbers and operands
                              "???":"???","???":"??","???":"??","???":"??","???":"???","???":"???","???":"???","???":"???","???":"???","???":"???",
                              "???":"???","???":"???","???":"???","???":"???","???":"???",
                              # Smalls latin
                              "a":"???","b":"???","c":"???","d":"???","???":"???","f":"???","g":"???",
                              "???":"???","???":"???","???":"??","???":"???","???":"??","???":"???","???":"???",
                              "???":"???","???":"???","q":"???","???":"??","???":"??","???":"???","???":"???",
                              "???":"???","w":"??","???":"??","y":"??","z":"???",
                              # Capital latin
                              "???":"???","???":"???","????":"???","????":"???" ,"???":"???","????":"???" ,"????":"???",
                              "???":"???","???":"???","???":"???","???":"???","???":"???","???":"???","???":"???",
                              "???":"???","???":"???","???":"???","???":"???","???":"??","???":"???","???":"???",
                              "???":"???","????":"???","???":"??","???":"??","????":"???",
                              # Smalls greek
                              "??":"???","???":"???","???":"???","??":"??","??":"???","??":"???","???":"???","???":"???",
                              "???":"??","???":"???","??":"??","??":"???","???":"???","??":"??","??":"??","???":"???",
                              "???":"???","??":"??","??":"??","??":"??","???":"??","??":"??","??":"??","???":"??",
                              "???":"???","??":"??","??":"??","???":"???","??":"??","??":"??",
                              # Capital greek
                              "???":"???","???":"???","??":"??","??":"???","???":"???","???":"???","???":"???","???":"???",
                              "???":"???","???":"???","??":"^","???":"???","???":"???","???":"???","??":"??","??":"??",
                              "???":"???","??":"??","???":"???","???":"??","??":"??","??":"??","???":"???","??":"??","????":"???"}

superscripts_to_subscripts = {# Numbers and operands
                              "???":"???","??":"???","??":"???","??":"???","???":"???","???":"???","???":"???","???":"???","???":"???","???":"???",
                              "???":"???","???":"???","???":"???","???":"???","???":"???",
                              # Smalls latin
                              "???":"a","???":"b","???":"c","???":"d","???":"???","???":"f","???":"g",
                              "???":"???","???":"???","??":"???","???":"???","??":"???","???":"???","???":"???",
                              "???":"???","???":"???","???":"q","??":"???","??":"???","???":"???","???":"???",
                              "???":"???","??":"w","??":"???","??":"y","???":"z",
                              # Capital latin
                              "???":"???","???":"???","???":"????","???":"????" ,"???":"???","???":"????","???":"????",
                              "???":"???","???":"???","???":"???","???":"???","???":"???","???":"???","???":"???",
                              "???":"???","???":"???","???":"???","???":"???","??":"???","???":"???","???":"???",
                              "???":"???","???":"????" ,"??":"???","??":"???","???":"????",
                              # Smalls greek
                              "???":"??","???":"???","???":"???","??":"??","???":"??","???":"??","???":"???","???":"???",
                              "??":"???","???":"???","??":"??","???":"??","???":"???","??":"??","??":"??","???":"???",
                              "???":"???","??":"??","??":"??","??":"??","??":"???","??":"??","??":"??","??":"???",
                              "???":"???","??":"??","??":"??","???":"???","??":"??","??":"??",
                              # Capital greek
                              "???":"???","???":"???","??":"??","???":"??","???":"???","???":"???","???":"???","???":"???",
                              "???":"???","???":"???","^":"??","???":"???","???":"???","???":"???","??":"??","??":"??",
                              "???":"???","??":"??","???":"???","??":"???","??":"??","??":"??","???":"???","??":"??","???":"????"}

small_to_caps = {# Latin
                 "a":"A","b":"B","c":"C","d":"D","e":"E","f":"F","g":"G",
                 "h":"H","i":"I","k":"K","l":"L","m":"M","n":"N","o":"O",
                 "p":"P","q":"Q","r":"R","s":"S","t":"T","u":"U","v":"V",
                 "w":"W","x":"X","y":"Y","z":"Z",
                 # Superscripts latin
                 "???":"???","???":"???","???":"???","???":"???","???":"???","???":"???","???":"???",
                 "???":"???","???":"???","??":"???","???":"???","??":"???","???":"???","???":"???",
                 "???":"???","???":"???","???":"???","??":"???","??":"??","???":"???","???":"???",
                 "???":"???","??":"???","??":"??","??":"??","???":"???",
                 # Subscripts latin
                 "a":"???","b":"???","c":"????","d":"????" ,"???":"???","f":"????","g":"????",
                 "???":"???","???":"???","???":"???","???":"???","???":"???","???":"???","???":"???","???":"???",
                 "???":"???","q":"???","???":"???","???":"???","???":"???","???":"???","???":"???","w":"????",
                 "???":"???","y":"???","z":"????",
                 # Greek
                 "??":"??","??":"??","??":"??","??":"??","??":"??","??":"??","??":"??",
                 "??":"??","??":"??","??":"??","??":"??","??":"??","??":"??","??":"??",
                 "??":"??","??":"??","??":"??","??":"??","??":"??","??":"??","??":"??",
                 "??":"??","??":"??","??":"??","??":"??","??":"??","??":"??","??":"??","??":"??",
                 # Superscripts greek
                 "???":"???","???":"???","???":"???","??":"??","???":"???","???":"???","???":"???",
                 "???":"???","??":"???","???":"???","??":"???","???":"???","???":"???","??":"^",
                 "??":"???","???":"???","???":"???","??":"??","??":"??","??":"??","??":"???",
                 "??":"??","??":"??","??":"???","???":"??","??":"??","??":"??","???":"???",
                 "??":"??","??":"???",
                 # Subscripts greek
                 "??":"???","???":"???","???":"???","??":"??","??":"??","??":"???","???":"???",
                 "???":"???","??":"???","??":"???","???":"???","??":"??","??":"???","???":"???",
                 "???":"???","??":"??","??":"??","??":"??","???":"???","??":"??","??":"??",
                 "???":"???","???":"???","??":"??","??":"??","???":"???","??":"??","??":"????",
                 }

caps_to_small = {# Latin
                 "A":"a","B":"b","C":"c","D":"d","E":"e","F":"f","G":"g",
                 "H":"h","I":"i","K":"k","L":"l","M":"m","N":"n","O":"o",
                 "P":"p","Q":"q","R":"r","S":"s","T":"t","U":"u","V":"v",
                 "W":"w","X":"x","Y":"y","Z":"z",
                 # Superscrips latin
                 "???":"???","???":"???","???":"???","???":"???","???":"???","???":"???","???":"???",
                 "???":"???","???":"???","???":"??","???":"???","???":"??","???":"???","???":"???",
                 "???":"???","???":"???","???":"???","???":"??","??":"??","???":"???","???":"???",
                 "???":"???","???":"??","??":"??","??":"??","???":"???",
                 # Subscripts latin
                 "???":"a","???":"b","????":"c","????":"d","???":"???","????":"f","????":"g",
                 "???":"???","???":"???","???":"???","???":"???","???":"???","???":"???","???":"???",
                 "???":"???","???":"???","???":"q","???":"???","???":"???","???":"???","???":"???",
                 "???":"???","????":"w","???":"???","???":"y","????":"z",
                 # Greek 
                 "??":"??","??":"??","??":"??","??":"??","??":"??","??":"??","??":"??",
                 "??":"??","??":"??","??":"??","??":"??","??":"??","??":"??","??":"??",
                 "??":"??","??":"??","??":"??","??":"??","??":"??","??":"??","??":"??",
                 "??":"??","??":"??","??":"??","??":"??",
                 # Superscripts greek
                 "???":"???","???":"???","??":"??","???":"???","???":"???","???":"???","???":"??",
                 "???":"??","???":"???","???":"???","^":"??","???":"??","???":"???","???":"???",
                 "??":"??","??":"??","???":"??","??":"??","???":"??","??":"???","??":"??",
                 "??":"??","???":"???","??":"??","???":"??",
                 # Subscripts greek
                 "???":"??","???":"???","??":"??","??":"??","???":"??","???":"???","???":"???",
                 "???":"??","???":"??","???":"???","??":"??","???":"??","???":"???","???":"???",
                 "??":"??","??":"??","???":"???","??":"??","???":"???","???":"???","??":"??",
                 "??":"??","???":"???","??":"??","????":"??"
                 }

#TODO softer checks for starting and ending formats
def maping(arg:str,transformation:str="superscripts",default_fill:str=" ",/,checks:bool=True):
    """maping Transforms a string to desired format

    Args:
        arg (str): String you want to convert
        transformation (str, optional): end format (in alls[4:14]). Defaults to "superscripts".
        default_fill (str, optional): caracter if no caracter is found. Defaults to " ".
        checks (bool, optional): if enabled perfom checks on types, set to False to increase performance. Defaults to True.

    Returns:
        _type_: trasnformed string and default_fill when translation isn't possible
    """    
    # Filter entryes
    if checks:
        if type(arg) != str:
            raise TypeError("Argument to convert must be string type (found %s)"%(type(arg)))
        if type(transformation)!= str:
            raise TypeError("Formating (transformation) must be string type (found %s)"%(type(transformation)))
        if type(default_fill) != str:
            raise TypeError("Default fill caracter must be string type(found %s)"%(type(default_fill)))
        transformation = transformation.lower()
        if transformation not in "".join(alls[4:14]):
            raise ValueError("Formating (transformation) must be a valid format (see all valid formats in %s.alls[4:14] list (found %s)"%(__name__,transformation))

    # Code for maping
    result = " "
    for i in arg:# all caracters in string
        try: 
            result += eval(transformation+".get('%s','%s')"%(i,default_fill)) 
        except : # if key doesn't exist
            result += default_fill
    return result

# End of library