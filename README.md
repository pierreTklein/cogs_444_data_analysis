# Data Analysis

## Data format

The format of the data is a `.csv` file with the following headers: `numHelped`,`crowdSize`,`sessionsCompleted`,`difficulty`, and `comfort`. The rows must be numerical. Examples of this data can be found in the [`sample_data`](/sample_data) directory.

## Analyzing the data

Place two files in a directory called `data`, named `method_1.csv`, and `method_2.csv`. Then, run the following command:

```bash
python analyze.py
```

The output will be the Matt Whitney U Test Results for the 5 questions:

```sh
+-----------------------------+
| Matt Whitney U Test Results |
+----------------+------------+-------------------------+
|        Question|   Statistic|                  P-Value|
+----------------+------------+-------------------------+
|   Number Helped|       XXX.X|                     X.XX|
|      Crowd Size|       XXX.X|                     X.XX|
|       Completed|       XXX.X|                     X.XX|
|      Difficulty|       XXX.X|                     X.XX|
|         Comfort|       XXX.X|                     X.XX|
+----------------+------------+-------------------------+
```

## Generating Box-plot data

The script to generate the box plot is written in `R`. Please download the proper package [here](https://cran.rstudio.com). Then, run the following command in the root directory:

```bash
Rscript gen_boxplot.r
```

It should save the box plots in a pdf file.