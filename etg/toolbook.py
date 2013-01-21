#---------------------------------------------------------------------------
# Name:        etg/toolbook.py
# Author:      Robin Dunn
#
# Created:     18-Jun-2012
# Copyright:   (c) 2013 by Total Control Software
# License:     wxWindows License
#---------------------------------------------------------------------------

import etgtools
import etgtools.tweaker_tools as tools

PACKAGE   = "wx"   
MODULE    = "_core"
NAME      = "toolbook"   # Base name of the file to generate to for this script
DOCSTRING = ""

# The classes and/or the basename of the Doxygen XML files to be processed by
# this script. 
ITEMS  = [ "wxToolbook",
           ]    
    
#---------------------------------------------------------------------------

def run():
    # Parse the XML file(s) building a collection of Extractor objects
    module = etgtools.ModuleDef(PACKAGE, MODULE, NAME, DOCSTRING)
    etgtools.parseDoxyXML(module, ITEMS)
    
    #-----------------------------------------------------------------
    # Tweak the parsed meta objects in the module object as needed for
    # customizing the generated code and docstrings.
    
    module.addHeaderCode('#include <wx/toolbook.h>')
    
    c = module.find('wxToolbook')
    assert isinstance(c, etgtools.ClassDef)
    tools.fixWindowClass(c)
    tools.fixBookctrlClass(c)
    
    module.addPyCode("""\
        EVT_TOOLBOOK_PAGE_CHANGED  = wx.PyEventBinder( wxEVT_COMMAND_TOOLBOOK_PAGE_CHANGED, 1 )
        EVT_TOOLBOOK_PAGE_CHANGING = wx.PyEventBinder( wxEVT_COMMAND_TOOLBOOK_PAGE_CHANGING, 1 )
        """)
    
    
    #-----------------------------------------------------------------
    tools.doCommonTweaks(module)
    tools.runGenerators(module)
    
    
#---------------------------------------------------------------------------
if __name__ == '__main__':
    run()

