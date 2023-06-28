""" Performs conversion between different temperature scales. """

SHIFT = 3
COMMENT = '#'
climate_data = open('data/sc_climate_data_10.csv', 'r')


def fahr_to_celsius(fahr):
    """COnverts fahrenehit to celsius

    Args:
        fahr (float): temperature in fahrenheit

    Returns:
        float: temperature in Celsius
    """
    celsius = ((fahr - 32) * (5/9)) 
    return celsius
def fahr_to_kelvin(fahr):
    """Converts fahrenehit to kelvin

    Args:
        fahr (float): temperature in fahrenheit

    Returns:
        float: temperature in kelvin
    """
    kelvin = fahr_to_celsius(fahr) + 273.15
    return kelvin



for line in climate_data:
    data = line.split(',')
    if data[0][0] != COMMENT:
        fahr = float(data[3])
        celsius = fahr_to_celsius(fahr)
        kelvin = fahr_to_kelvin(fahr)
        print('Max temperature in Celsius', celsius, 'Kelvin', kelvin)
