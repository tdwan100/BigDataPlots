# Earthquake Magnitude vs. Depth Analysis

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project analyzes earthquake data obtained from the USGS (United States Geological Survey) and explores the relationship between earthquake magnitudes and depths. The data is retrieved from the USGS earthquake feed API, and the analysis is performed using Python.

## Requirements

To run the code and reproduce the analysis, you will need the following:

- Python 3.x
- Matplotlib
- NumPy
- Requests (for fetching data from the API)

## Installation

1. Clone this repository to your local machine:

```
git clone https://github.com/your-username/BigDataPlots.git
cd BigDataPlots
```

2. Install the required Python packages:

```
pip install matplotlib numpy requests
```

## Usage

1. Run the Python script `BigDataPlots.py`:

```
python BigDataPlots.py
```

2. The script will fetch earthquake data from the USGS API, calculate the Pearson correlation coefficient between magnitude and depth, and plot the graph. The graph will show the linear regression fit and the scatter plot of earthquake magnitudes vs. depths.

## Results

The plotted graph will display the correlation between earthquake magnitudes and depths. The red line represents the linear regression fit, showing the general trend of the data. Additionally, there will be a text annotation showing the Pearson correlation coefficient, indicating the strength of the relationship.

## Contributing

Contributions to this project are welcome! If you find any issues or have ideas for improvement, feel free to open an issue or submit a pull request.

## Acknowledgments

- The earthquake data used in this project is provided by the USGS (United States Geological Survey). Visit their website at [https://earthquake.usgs.gov](https://earthquake.usgs.gov) for more information.
