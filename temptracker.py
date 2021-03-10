'''
This script requires python 3.4 or higher
'''
#import random
import statistics

class TempTracker(object):
    '''
    args: *args
    type: list
    '''

    MIN_TEMP=0
    MAX_TEMP=111

    def __init__(self, *args):
        if len(args)>1:
            raise TypeError('Too many arguments passed to TempTracker, pass one list argument(ex: [4, 50, 101])')
        self.temperatures=args[0]
        #self.temperatures=existing_records

    @property
    def temperatures(self):
        return self._temperatures
    
    @temperatures.setter
    def temperatures(self, existing_records):
        if isinstance(existing_records, list):
            print ("Setting recorded temperatures")
            for value in existing_records:
                if value not in range(TempTracker.MIN_TEMP,TempTracker.MAX_TEMP):
                    print ("Value {0} not a whole number between 0 and 110, excluded from records".format(value))
                    #raise ValueError ("Value {0} not a number between 0 and 110, excluded from records".format(value))
                    existing_records.remove(value)               
            self._temperatures=existing_records
        else:
            raise TypeError('Make sure argument of TempTracker is a list. Ex: tp=TempTracker([2,45,70])')

    def args_amount(func):
        '''
        Decorator:
        checking the number of the arguments passed to the func method
        '''
        def wrapper(self, *args):
            if len(args)>1:
                print ("Too many arguments to insert, pass just one argument")
                return
            else:
                return func(self, *args)
        return wrapper

    @args_amount
    def insert(self, new_record):
        if new_record not in range(TempTracker.MIN_TEMP,TempTracker.MAX_TEMP):
            print ("Data {0} not a single whole number between 0 and 110, not included in records".format(new_record))
            #raise ValueError ("Value {0} not a number between 0 and 110, not included in records".format(new_record))
            return (self.temperatures)
        return self.temperatures.append(new_record)

    def records_exist(func):
        '''
        Decorator:
        checking that the self.temperatures has at least one number in it
        '''
        def wrapper(self):
            if not self.temperatures: 
                print ('No existing records, cannot get requested statistic data')
            else:
                return func(self)
        return wrapper

    @records_exist
    def get_max(self):
        return max(self.temperatures)

    @records_exist
    def get_min(self):
        return min(self.temperatures)

    @records_exist
    def get_mean(self):
        return statistics.mean(self.temperatures)

#tmpr = TempTracker([1,5,7,8], [101, 109])
#tmpr.insert(6,3,2)
#tmpr.insert(4)
#print(tmpr.temperatures)
#print(tmpr.get_max())
# tmpr.insert(11)
# tmpr.insert(11,56,91)
# print (tmpr.get_min())
# print (tmpr.temperatures)

# tmp = TempTracker([4, 400, 86, 103, 110, 111, 0, -15])
# print (tmp.temperatures)
# tmp.insert(67.65)
# tmp.insert('Hello')
# tmp.insert(502)
# tmp.insert((13))
# tmp.insert(73)
# print (tmp.temperatures)

# tmpr = TempTracker((5,78,90))
# print(tmpr.temperatures)







