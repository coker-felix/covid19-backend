import math
def computeForSevereImpact(data):
    average_Daily_Income_InUSD = data['region']['avgDailyIncomeInUSD']
    average_Daily_Income_population = data['region']['avgDailyIncomePopulation'] 
    time_to_elapse = data['timeToElapse']
    reported_cases = data['reportedCases']
    total_hospital_beds = data['totalHospitalBeds']
    period_type = data['periodType']


    if period_type == 'days':
        period = int(time_to_elapse)
    elif period_type == 'weeks':
        period = int(time_to_elapse * 7)
    elif period_type == 'months':
        period = int(time_to_elapse * 30)
    else:
        period = int(time_to_elapse * 360)

    factor = int(period//3)    

    # Make computations
    # CHALLENGE 1
    currentlyInfected = reported_cases * 50
    infectionsByRequestedTime = currentlyInfected * (2 ** factor)
    infectionsByRequestedTime = int(infectionsByRequestedTime)

    # CHALLENGE 2
    severeCasesByRequestedTime = (15/100) *  infectionsByRequestedTime
    severeCasesByRequestedTime = int(severeCasesByRequestedTime)
    hospitalBedsByRequestedTime  = ((35/100) * total_hospital_beds) - severeCasesByRequestedTime
    hospitalBedsByRequestedTime = int(hospitalBedsByRequestedTime)

    # CHALLENGE 2
    casesForICUByRequestedTime = (5/100) * infectionsByRequestedTime
    casesForICUByRequestedTime = int(casesForICUByRequestedTime)
    casesForVentilatorsByRequestedTime = (2/100) * infectionsByRequestedTime
    casesForVentilatorsByRequestedTime = int(casesForVentilatorsByRequestedTime)
    dollarsInFlight = math.trunc((infectionsByRequestedTime * average_Daily_Income_population * average_Daily_Income_InUSD )/ period)
    dollarsInFlight = int(dollarsInFlight)

    

    data = {}
    data['currentlyInfected'] = currentlyInfected
    data['infectionsByRequestedTime'] = infectionsByRequestedTime
    data['severeCasesByRequestedTime'] = severeCasesByRequestedTime
    data['hospitalBedsByRequestedTime'] = hospitalBedsByRequestedTime
    data['casesForICUByRequestedTime'] = casesForICUByRequestedTime
    data['casesForVentilatorsByRequestedTime'] = casesForVentilatorsByRequestedTime
    data['dollarsInFlight'] = dollarsInFlight
    severeResult = data
    return severeResult



