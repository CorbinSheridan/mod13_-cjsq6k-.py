import unittest
 #Symbol
def capitalized(text):
  if len(text) < 1 or len(text) > 7:
    raise ValueError('Text must be 1-7 characters') 
  if not text.isalpha():
    raise ValueError('Text must contain only alphabetic characters')
  return text.upper()

class TestCapitalized(unittest.TestCase):

  def test_valid(self):
    self.assertEqual(capitalized('hello'), 'HELLO')
    self.assertEqual(capitalized('abcdefg'), 'ABCDEFG')

  def test_too_short(self):
    with self.assertRaises(ValueError):
      capitalized('')
  
  def test_too_long(self):
    with self.assertRaises(ValueError):
      capitalized('abcdefgh')

  def test_not_alpha(self):
    with self.assertRaises(ValueError):
      capitalized('hello1')

#Chart Type

def validate_chart_type(chart_type):
  if not isinstance(chart_type, str):
    raise TypeError('Chart type must be a string')
  
  if len(chart_type) != 1:
    raise ValueError('Chart type must be 1 character')
  
  if chart_type not in ['1', '2']:
    raise ValueError('Chart type must be 1 or 2')
  
  return chart_type

class TestValidateChartType(unittest.TestCase):

  def test_valid(self):
    self.assertEqual(validate_chart_type('1'), '1')
    self.assertEqual(validate_chart_type('2'), '2')

  def test_not_string(self):
    with self.assertRaises(TypeError):
      validate_chart_type(1)

  def test_too_long(self):
    with self.assertRaises(ValueError):
      validate_chart_type('12')

  def test_invalid_value(self):
    with self.assertRaises(ValueError):
      validate_chart_type('3')


#Time Series

def validate_time_series(time_series):
  if not isinstance(time_series, str):
    raise TypeError('Time series must be a string')

  if not time_series.isdigit():
    raise ValueError('Time series must contain only digits')

  if len(time_series) < 1 or len(time_series) > 4:
    raise ValueError('Time series must be 1 to 4 digits')

  return time_series

class TestValidateTimeSeries(unittest.TestCase):

  def test_valid(self):
    self.assertEqual(validate_time_series('1'), '1')
    self.assertEqual(validate_time_series('1234'), '1234')

  def test_not_string(self):
    with self.assertRaises(TypeError):
      validate_time_series(123)

  def test_not_digits(self):
    with self.assertRaises(ValueError):
      validate_time_series('abc')

  def test_too_short(self):
    with self.assertRaises(ValueError):
      validate_time_series('')
  
  def test_too_long(self):
    with self.assertRaises(ValueError):
      validate_time_series('12345')

 #Start Date
from datetime import datetime

def validate_start_date(start_date):
  try:
    datetime.strptime(start_date, '%Y-%m-%d')
  except ValueError:
    raise ValueError('Invalid date format. Must be YYYY-MM-DD')
  
  return start_date

class TestValidateStartDate(unittest.TestCase):

  def test_valid(self):
    self.assertEqual(validate_start_date('2020-01-01'), '2020-01-01')

  def test_invalid_format(self):
    with self.assertRaises(ValueError):
      validate_start_date('01-01-2020')
  
  def test_invalid_day(self):
    with self.assertRaises(ValueError):
      validate_start_date('2020-02-30')
  
  def test_invalid_month(self):
    with self.assertRaises(ValueError):
      validate_start_date('2020-13-01')

#End Date
def validate_end_date(end_date):
  try: 
    datetime.strptime(end_date, '%Y-%m-%d')
  except ValueError:
    raise ValueError('Invalid date format. Must be YYYY-MM-DD')
  
  return end_date

class TestValidateEndDate(unittest.TestCase):

  def test_valid(self):
    self.assertEqual(validate_end_date('2020-12-31'), '2020-12-31')
  
  def test_invalid_format(self):
    with self.assertRaises(ValueError):
      validate_end_date('12-31-2020')

  def test_invalid_day(self):
    with self.assertRaises(ValueError):  
      validate_end_date('2020-11-31')
  
  def test_invalid_month(self):
    with self.assertRaises(ValueError):
      validate_end_date('2020-15-01')

if __name__ == '__main__':
  unittest.main()