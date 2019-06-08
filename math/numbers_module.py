# -*- coding: utf-8 -*-

class Numbers:
    '''class representing Numbers,
       implements a high precision representation
       of the decimal part of floating point numbers
       
       
       Methods:
        - precision
        - format_n
        - format_nargs
        - integer
        - integers
        - floating
        - string
        - __test
        - _TEST_CLASS
    '''
    
    _DEFAULT_PRECISION = 5
    
    def __init__(self,precision=_DEFAULT_PRECISION):
        '''REQUIRES: optional precison (decimal part length)
           MODIFIES: self
           EFFECT:   constructor, set length of decimal part
                     or DEFAULT = 5
        '''
        self._precision = int(str(precision).replace('-','')
                                            .replace('.',''))
    #END __init__
    
    
    def precision(self,precision):
        '''REQUIRES: precison (decimal part length)
           MODIFIES: self
           EFFECT:   set length of decimal part
        '''
        self._precision = int(str(precision).replace('-',''))
    #END precision
    
    
    def format_n(self,number):
        '''REQUIRES: number
           MODIFIES: self
           EFFECT:   returns a string representing the formatted float number
        '''
            
        if number == None:
            return None
        
        self.__number = ''
        
        if type(number) == type(int()):
            self.__number = str(number) + '.0'
        elif type(number) == type(float()):
            self.__number = str(number)
        elif type(number) == type(str()):
#            print(number)
#            self.__test(type(float(number)) == type(float()), 'Not a Number')
            if number.split('.')[0] == '':
                self.__number += '0' + number
            if number.count('.') == 0:
                self.__number += number + '.0'
            else:
                self.__number += number
                
        self.__int = self.__number.split('.')[0]
        self.__decimals = self.__number.split('.')[1]
        self.__decimals = (self.__decimals+('0'*(self._precision-len(self.__decimals))) 
                    if len(self.__decimals) < self._precision else self.__decimals[0:self._precision])
        return f'{self.__int}.{self.__decimals}'
    #END format_n
    
    
    def format_nargs(self,*args):
        '''REQUIRES: *args
           MODIFIES: self
           EFFECT:   returns an array of string formatted float numbers
        '''
        self.__f_nargs = []
        for number in args:
            self.__f_narg = '0.0'
            
            if number == None:
                self.__f_narg = None
                self.__f_nargs.append(self.__f_narg)
                continue
            
            if type(number) == type(int()):
                self.__f_narg = str(number) + '.0'
            elif type(number) == type(float()):
                self.__f_narg = str(number)
            elif type(number) == type(str()):
                self.__test(type(float(number)) == type(float()), 'Not a Number')
                if number.split('.')[0] == '':
                    self.__f_narg += '0' + number
                if number.count('.') == 0:
                    self.__f_narg += number + '.0'
                else:
                    self.__f_narg += number
            
            self.__int = self.__f_narg.split('.')[0]
            self.__decimals = self.__f_narg.split('.')[1]
            self.__decimals = (self.__decimals+('0'*(self._precision-len(self.__decimals))) 
                        if len(self.__decimals) < int(self._precision)
                        else self.__decimals[0:self._precision])
            self.__f_nargs.append(f'{self.__int}.{self.__decimals}')
        return self.__f_nargs
    #END format_nargs
    
    
    def integer(self,number):
        '''REQUIRES: number
           MODIFIES: self
           EFFECT:   returns an integer truncating the decimal part
        '''
        if number == None:
            return None
        elif type(number) == type(int()):
            return number
        elif type(number) == type(float()):
            return int(number)
        elif type(number) == type(str()):
            if number.split('.')[0] == '':
                return 0
            return int(float((number + '.0').split('.')[0]))
        else:
            self.__test(type(float(str(number))) == type(float()), 'Not a Number')
        return self.integer(float(str(number)))
    #END integer
    
    
    def integers(self,*args):
        '''REQUIRES: *args
           MODIFIES: self
           EFFECT:   returns an array of integers truncating the decimal part
        '''
        self.__args = []
        for number in args:
            if number == None:
                pass
            elif type(number) == type(int()):
                pass
            elif type(number) == type(float()):
                number = int(number)
            elif type(number) == type(str()):
                if number.split('.')[0] == '':
                    number = '0'
                number = int(float((number + '.0').split('.')[0]))
            else:
                self.__test(type(float(str(number))) == type(float()), 'Not a Number')
                number = self.integer(float(str(number)))
            self.__args.append(number)
        return self.__args
    #END integers
    
    
    def floating(self,number):
        '''REQUIRES: number
           MODIFIES: 
           EFFECT:   return a formatted float number
        '''
        if number == None:
            return None
        number = self.format_n(number)
        return float(number)
    #END floating
        
    
    def string(self,number):
        '''REQUIRES: number
           MODIFIES: 
           EFFECT:   return the string representation of a number
        '''
        if number == None:
            return None
        elif type(number) == type(str()):
            self.__test(type(float(number)) == type(float()), 'Not a Number')
            if number.split('.')[0] == '':
                return '0' + number
        elif type(number) == type(int()):
            return str(number)
        elif type(number) == type(float()):
            return str(self.floating(number))
        self.__test(type(float(str(number))) == type(float()), 'Not a Number')
        return str(number)
    #END string
    

    def __test(self,condition,msg=True):
        '''REQUIRES: condition: prediacate
                     msg:       message to print when test fails
           MODIFIES: 
           EFFECT:   checks whether a condition is True,
                     an AssertionException is rised if the test fails
        '''
        try:
            assert condition, f'expected {msg}, but found: {condition}'
        except AssertionError as e:
            print(f'Your test FAILED: {e}')
    #END __test
    
    
    def _TEST_CLASS():
        '''REQUIRES: 
           MODIFIES: 
           EFFECT:   tests cases
        '''
        print('\n------Numbers._TEST_CLASS()------\n')
        n = Numbers(5)
        
        n.precision(10)
        
        print(Numbers._DEFAULT_PRECISION)
        print()
        
        print(n.integer(5))
        print(n.integer(0.5))
        print(n.integer(5.0))
        print(n.integer('5'))
        print(n.integer('.5'))
        print(n.integer('1.5'))
        print(n.integer(Numbers._DEFAULT_PRECISION))
        print()
        
        print(n.integers(5))
        print(n.integers(5.5,'7.7'))
        print(n.integers(5.5,'7.7','',None))
        print(n.integers(5.0))
        print(n.integers('5'))
        print(n.integers('.5'))
        print(n.integers('1.5'))
        print(n.integers(Numbers._DEFAULT_PRECISION))
        print()
        
        print(n.string(5))
        print(n.string(5.5))
        print(n.string(.5))
        print(n.string(0.5))
        print(n.string('5'))
        print(n.string('5.0'))
        print(n.string('.5'))
        print(n.string('0.5'))
        print(n.string(Numbers._DEFAULT_PRECISION))
        #print(n.string('a.5'))
        print()
        
        print(n.format_n(5))
        print(n.format_n(5.5))
        print(n.format_n(.5))
        print(n.format_n(0.5))
        print(n.format_n('5'))
        print(n.format_n('5.5'))
        print(n.format_n('.5'))
        print(n.format_n('0.5'))
        print(n.format_n(Numbers._DEFAULT_PRECISION))
        print()
        
        print(n.format_nargs(5,7))
        print(n.format_nargs(5.5,7.7))
        print(n.format_nargs(.5,.7))
        print(n.format_nargs(0.5,0.7))
        print(n.format_nargs('5','7'))
        print(n.format_nargs('5.5','7.7'))
        print(n.format_nargs('.5','.7'))
        print(n.format_nargs('0.5','0.7'))
        print(n.format_nargs(Numbers._DEFAULT_PRECISION))
        print()
        
        
        n.precision(4)
        print(n.floating(5))
        print(n.floating(5.5000123))
        print(n.floating(.5432101))
        print(n.floating(0.5))
        print(n.floating('5'))
        print(n.floating('5.5123456'))
        print(n.floating('.56543210'))
        print(n.floating('0.5'))
        print(n.floating(Numbers._DEFAULT_PRECISION))
        print('\n------END------\n')
    #END _TEST_CLASS



# TEST
Numbers._TEST_CLASS()
