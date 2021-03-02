import pandas as pd

def read_percentiles(percentiles_file):
  percentiles = pd.read_csv(percentiles_file, dtype={'Agemos': float, 'P5': float,
    'P50': float, 'P95': float, 'L': float, 'M': float, 'S': float, 'Sex': int})
  percentiles['age'] = percentiles['Agemos'] / 12
  # Values by CDC (1=male; 2=female) differ from growthcleanr
  # which uses a numeric value of 0 (male) or 1 (female).
  # This aligns things to the growthcleanr values
  percentiles['Sex'] = percentiles['Sex'] - 1
  return percentiles