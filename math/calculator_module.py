# -*- coding: utf-8 -*-

from numbers_module import Numbers

class Calculator(Numbers):
    '''extending Numbers class, this class implements methods
       to perform basic operations with high precision floating
       point numbers
       
       Methods:
        - nargs_sum
        - nargs_mult
        - nargs_div
        - int_str
        - str_float
        - test
        - remove_tail_zeros
        - last_non_zero_index
        - non_zero_index
        - _TEST_CLASS
    '''
    
    def __init__(self):
        '''REQUIRES: ---
           MODIFIES: self
           EFFECT:   constructor, initializes floating point precision = 5
        '''
        self.__n = Numbers()
        self.__n.precision(Calculator._DEFAULT_PRECISION)
        
        
    
    def nargs_sum(self,*args):
        '''REQUIRES: *args
           MODIFIES: self
           EFFECT:   returns the string representing the float formatted sum
                     of a list of numbers
        '''
        self.__sum = '#init#'
        for arg in args:
            #prepare
            if self.__sum == '#init#':
                self.__sum = str(self.__n.format_n(arg))
                if len(args) == 1:
                    return self.__sum
                continue
            else:
                arg = str(self.__n.format_n(arg))
            
            if arg == None or self.__sum == None:
                continue
            
            #remove floating point, add int values
            self.__sum = str(int(self.__sum.replace('.',''))
                          + int(arg.replace('.','')))
            
            #reset floating point
            self.__sum = f'{self.__sum[0:-self.__n._precision]}.'\
                         f'{self.__sum[-self.__n._precision:]}'
        return self.__n.format_n(self.__sum)
      #END nargs_sum    
        
        
    
    def nargs_mult(self,*args):
        '''REQUIRES: *args
           MODIFIES: self
           EFFECT:   returns the product of the formatted number list
        '''
        self.__prod = '#init#'
        for arg in args:
            if self.__prod == '#init#':
                self.__prod = str(float(arg))
                if len(args) == 1:
                    return self.__prod
                continue
            
            
            if arg == None or self.__prod == None:
                self.__prod = None
                continue
            
            arg = self.str_float(arg)
            
            #len decimal part
            self.__fa = len(arg.split('.')[1])
            self.__fp = len(self.__prod.split('.')[1])
            self.__decimal = self.__fa + self.__fp
            
            #as int
            self.__arg_as_int = int(arg.replace('.',''))
            self.__prod_as_int = int(self.__prod.replace('.',''))
            
            #int product
            self.__prod = str(self.__arg_as_int * self.__prod_as_int)
        
            #reset decimals in product
            if self.__decimal < len(self.__prod):
                self.__prod = ''\
                    f'{self.__prod[0:(len(self.__prod)-self.__decimal)]}.'\
                    f'{self.__prod[(len(self.__prod)-self.__decimal):]}'
            elif self.__decimal > len(self.__prod):
                self.__zeros = '0'*(self.__decimal - len(self.__prod))
                self.__prod = f'0.{self.__zeros}{self.__prod}'
            else:
                self.__prod = f'0.{self.__prod}'
        
        return self.__n.format_n(self.__prod)
    #END nargs_mult
        

    def nargs_div(self,*args):
        '''REQUIRES: *args
           MODIFIES: self
           EFFECT:   returns the result of the division by each formatted number
                     within the list
        '''
        self.__result = '#init#'
        self.__reminder = 0
        for divisor in args:
            #prepare
            if self.__result == '#init#':
                self.__result = self.__n.format_n(divisor)
                if len(args) == 0:
                    return None
                if len(args) == 1:
                    return self.__result
                continue
            else:
                divisor = self.__n.format_n(divisor)
            
            if divisor == None or self.__result == None:
                self.__result = None
                continue
            self.__dividend = self.__result
            
            #operation sign
            self.__sign_dividend = -1 if self.__dividend[0] == '-'  else 1
            self.__sign_divisor = -1 if divisor[0] == '-' else 1
            self.__sign = ('' 
                           if self.__sign_dividend * self.__sign_divisor == 1 
                           else '-')
            
            #remove sign and floating point
            self.__int_dividend = int(self.__dividend
                                          .replace('-','')
                                          .replace('.',''))
            self.__int_divisor = int(divisor.replace('-','')
                                            .replace('.',''))
            
            #int division and reminder
            self.__result = f'{self.__sign}'\
                            f'{self.__int_dividend // self.__int_divisor}'
            self.__reminder = (self.__int_dividend % self.__int_divisor)
            
            #decimal part
            if self.__reminder != 0:
                self.__result += '.'
                for i in range(self.__n._precision):
                    if self.__reminder == 0:
                        break
                    if self.__reminder < self.__int_divisor:
                        self.__reminder *= 10
                    self.__int_dividend = self.__reminder // self.__int_divisor
                    self.__reminder = self.__reminder % self.__int_divisor
                    self.__result += str(self.__int_dividend)
                    
            self.__result = self.__n.format_n(self.__result)
        return self.__result
    #END nargs_div
    
    
    def int_str(self,string_num):
        '''REQUIRES: string_num
           MODIFIES: ---
           EFFECT:   returns the int value of a string representation of a number
        '''
        if type(string_num) == type(int()):
            return string_num
        elif type(string_num) == type(float()):
            string_num = str(string_num)
        elif type(string_num) != type(str()):
            self.test(type(float(string_num)) == type(float()),'Not a number')
        return int(string_num.split('.')[0])
    #END int_str 
        
    
    
    def str_float(self,num):
        '''REQUIRES: num
           MODIFIES: ---
           EFFECT:   returns a string representing the float value of a number
        '''
        if type(num) == type(int()):
            return str(num) + '.0'
        elif type(num) == type(float()):
            return str(num)
        elif type(num) == type(str()):
            self.test(type(float(num)) == type(float()),'Not a number')
            return num
        else:
            self.test(type(float(str(num))) == type(float()),'Not a number')
            return self.str_float(str(num))
    #END str_float


    def test(self,condition,msg=True):
        '''REQUIRES: condition: predicate
                     msg:       message to print if test fails
           MODIFIES: ---
           EFFECT:   checks if condition is True or rises an AssertionException
        '''
        try:
            assert condition, f'expected {msg}, but found: {condition}'
        except AssertionError as e:
            print(f'Your test FAILED: {e}')
    #END test
    
    
    def remove_tail_zeros(self,string_num):
        '''REQUIRES: string_num
           MODIFIES: ---
           EFFECT:   returns a string representing the decimal part of a number
                     without exceeding zeros
        '''
        string_num = ('' if int(self.str_float(string_num).split('.')[1]) == 0 
                               else self.str_float(string_num).split('.')[1])
        return (string_num[0:self.last_non_zero_index(string_num)])
    #END remove_tail_zeros
    
    
    def last_non_zero_index(self,num):
        '''REQUIRES: num
           MODIFIES: ---
           EFFECT:   returns the length of the string formatted number (index + 1)
                     at last non zero digit, '.' is counted too
        '''
        if type(num) == type(float()) or type(num) == type(int()):
            num = str(num)
            
        self.last_non_zero_idx = 0
        for i in range(len(num))[-1::-1]:
            if num[i] == '0':
                continue
            else:
                self.last_non_zero_idx = i + 1
                break
        return self.last_non_zero_idx
    #END last_non_zero_index
            
        
    def non_zero_index(self,num):
        '''REQUIRES: num
           MODIFIES: ---
           EFFECT:   returns the length of the string formatted number (index + 1)
                     at first non zero digit, '.' is counted too
        '''
        if type(num) == type(float()) or type(num) == type(int()):
            num = str(num)
            
        self.__non_zero_idx = 0
        for i in range(len(num)):
            if num[i] == '0':
                self.__non_zero_idx = i + 1
            elif num[i] != '0':
                break
        return self.__non_zero_idx
    #END non_zero_index
    
    
    def _TEST_CLASS():
        '''REQUIRES: ---
           MODIFIES: ---
           EFFECT:   test cases
        '''
        print('\n------Numbers._TEST_CLASS()------\n')
            
        c = Calculator()
        
        print('remove_zeros')
        print(f'decimal -> remove zeros: {c.remove_tail_zeros(10.0)}')
        print(f'decimal -> remove zeros: {c.remove_tail_zeros(10.010)}')
        print()
        
        print('str_float')
        print(c.str_float(123))
        print(c.str_float(123.456))
        print(c.str_float('123.456'))
        
#        print(c.str_float('123.456a'))
#        print(c.str_float(''))
        
        print('\nDivision:')
        print(f'>> div: {c.nargs_div(-10,3)}')
        print(f'>> div: {c.nargs_div(10,3)}')
        print(f'>> div: {c.nargs_div(3,10)}')
        print(f'>> div: {c.nargs_div(3,-10)}')
        print(f'>> div: {c.nargs_div(-120,-5,-4,-3)}')
        print(f'>> div: {c.nargs_div(120,5,-4,3)}')
        print(f'>> div: {c.nargs_div(-120,5,-4,-3)}')
        print(f'>> div: {c.nargs_div(120,5,4,3)}')
        print(f'>> div: {c.nargs_div(24,4)}')
        print(c.nargs_div(0.3,10))
        print(c.nargs_div(10, 0.300))
        print(c.nargs_div(1, 0.03))
        print(c.nargs_div(1, 0.0030))
        print()
        print(100%3)
        print(c.last_non_zero_index(1020))
        print()
        
        c.__n.precision(10)
        print('PRECISION: 10\n')
        
        print('Multiplication:')
        print(c.nargs_mult(1.2,3.4))
        print(c.nargs_mult(12,3.4))
        print(c.nargs_mult(12,34))
        print(c.nargs_mult(0.12,34))
        print(c.nargs_mult(1.2,0.34))
        print(c.nargs_mult(0.12,0.34))
        print(c.nargs_mult(0.012,0.34))
        print(c.nargs_mult(0.012,0.034))
        print(c.nargs_mult(-1,1,2,3,4,5))
        print(c.nargs_mult(-1,1,2,3,-4,5))
        print(c.nargs_mult(-1,1,-2,3,-4,5))
        
        print('\ntype:')
        print(type(c.nargs_mult(-1,1,2,3,4,5)))
        
        print('\nformat_n:')
        print(c.__n.format_n('123'))
        print()
        
        a = c.__n.format_n(10.1091)
        b = c.__n.format_n(1.9019)
        print(f'{a}, {b}')
        print('>> sum :', c.nargs_sum(a,b))
        print('>> oper:',float(a)+float(b))
        print()
        
        
        c.__n.precision(4)
        print('PRECISION: 4\n')
        
        a = c.__n.format_n(10.00109)
        b = c.__n.format_n(1.00901)
        print(f'{a}, {b}')
        print('>> sum :', c.nargs_sum(a,b))
        print('>> oper:',float(a)+float(b))
        print()
        
        c.__n.precision(6)
        print('PRECISION: 6\n')
        
        a1 = c.__n.format_n(10.89111)
        b1 = c.__n.format_n(-1.11921)
        print(f'        {a1} +\n        {b1}')
        print('>> sum :',c.nargs_sum(a1,b1))
        print('>> oper:',float(a1)+float(b1))
        print()
        
        print(c.nargs_sum(1,2,3,4,5))
        print(f'>> sum: {c.nargs_sum(-1.101,2,3,4,5)}')
        print(c.nargs_sum(10.89111,-1.11921))
        print(f'>> sum: {c.nargs_sum(10.8911,1.1192)}')
        print()
        
        print(10.10*1.001)
        print('\n------END------\n')
    #END _TEST_CLASS

#TEST
Calculator._TEST_CLASS()
