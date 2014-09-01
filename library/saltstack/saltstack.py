"""ShutIt module. See http://shutit.tk
"""
#Copyright (C) 2014 OpenBet Limited
#
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is furnished
#to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
#FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
#COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
#IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
#CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from shutit_module import ShutItModule

class saltstack(ShutItModule):

    def is_installed(self,shutit):
        return False

    def build(self,shutit):
        shutit.install('curl')
        # Not working
        shutit.send('curl -L http://bootstrap.saltstack.org | sh -s -- -M -N')
        return True

    #def get_config(self,shutit):
    #    return True

    #def check_ready(self,shutit):
    #    return True
    
    #def start(self,shutit):
    #    return True

    #def stop(self,shutit):
    #    return True

    #def finalize(self,shutit):
    #    return True

    #def remove(self,shutit):
    #    return True

    #def test(self,shutit):
    #    return True

def module():
    return saltstack(
        'shutit.tk.saltstack.saltstack', 782914092.1235236,
        description='Saltstack master setup',
        maintainer='ian.miell@gmail.com',
        depends=['shutit.tk.setup']
    )
