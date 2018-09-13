
## Stats701 Homework 7, Winter 2018
### Pandas
### Katherine Wilkinson
#### kswilk@umich.edu

I discussed this homework with Sam Edds

#### 1. Warmup: Construction pandas objects


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

##### 1.1 
Create a pandas Series object with indices given by the first 10 letters of the English
alphabet and values given by the first 10 primes


```python
## Use prime generator from previous homework
def primes():
    #first prime is 2
    n = 2
    #create empty set to put primes in
    primes = set()
    while True:
        #loop through set
        for p in primes:
            #if n/p has no remainder, break while loop
            #that is, n is divisble by some number not itself or 1
            #print(n%p , n,p)
            if n % p == 0:
                break
        
        else:
            # if n%p != 0, add to primes set
            primes.add(n)
            #yield all n added to primes set
            yield n
        #add one to n 
        n = n + 1
p = primes()
#generate first 10 primes
p = [next(p) for _ in range(10)]
```


```python
# Create index for first 10 letters of alphabet
idx = ['a','b','c','d','e','f','g','h','i','j']
#Create pandas series
s = pd.Series(p, index = idx)

```




    a     2
    b     3
    c     5
    d     7
    e    11
    f    13
    g    17
    h    19
    i    23
    j    29
    dtype: int64



##### 1.2
Below is a table that might arise in a genetics experiment. Reconstruct this as a
pandas DataFrame.


```python
## Create empty list to append values 1-12
score1 = []
for i in range(1,13):
    score1.append(i)

## create dictionary for score1 and score2
d = {'score1':pd.Series(score1),
    'score2':pd.Series([2,4,4,6,6,8,8,10,10,12,12,14])}

## create values for indices 
arrs = [['goat','goat','goat','goat','bird','bird',
        'bird','bird','llama','llama','llama','llama'],
        ['A','A','a','a','A','A','a','a','A','A','a','a'],
       ['A','a','A','a','A','a','A','a','A','a','A','a']]

##Arragne multiple indicies
idx = pd.MultiIndex.from_arrays(arrs, names = ['animal',
                                              'parent1', 'parent2'])

##Create series with score1 and above index
s = pd.Series(score1, index = idx)
d2 = {'score1':s}
#Make it dataframe
df = pd.DataFrame(d2)
##Add score2 to the data frame
df['score2'] = [2,4,4,6,6,8,8,10,10,12,12,14]
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th>score1</th>
      <th>score2</th>
    </tr>
    <tr>
      <th>animal</th>
      <th>parent1</th>
      <th>parent2</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">goat</th>
      <th rowspan="2" valign="top">A</th>
      <th>A</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>a</th>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">a</th>
      <th>A</th>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>a</th>
      <td>4</td>
      <td>6</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">bird</th>
      <th rowspan="2" valign="top">A</th>
      <th>A</th>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>a</th>
      <td>6</td>
      <td>8</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">a</th>
      <th>A</th>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>a</th>
      <td>8</td>
      <td>10</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">llama</th>
      <th rowspan="2" valign="top">A</th>
      <th>A</th>
      <td>9</td>
      <td>10</td>
    </tr>
    <tr>
      <th>a</th>
      <td>10</td>
      <td>12</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">a</th>
      <th>A</th>
      <td>11</td>
      <td>12</td>
    </tr>
    <tr>
      <th>a</th>
      <td>12</td>
      <td>14</td>
    </tr>
  </tbody>
</table>
</div>



#### 2. Working with pandas DataFrames

##### 2.1
Download the iris data set from the link above. Please include this file in your
submission. Read iris.csv into Python as a pandas DataFrame. Note that the
CSV file includes column headers. How many data points are there in this data set?
What are the data types of the columns? What are the column names? The column
names correspond to flower species names, as well as four basic measurements one
can make of a flower: the width and length of its petals and the width and length
of its sepal (the part of the pant that supports and protects the flower itself). How
many species of flower are included in the data?


```python
iris = pd.read_csv('iris.csv')
iris.info()
iris.head()
iris['Species'].unique()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 150 entries, 0 to 149
    Data columns (total 5 columns):
    Sepal.Length    150 non-null float64
    Sepal.Width     150 non-null float64
    Petal.Length    150 non-null float64
    Petal.Width     150 non-null float64
    Species         150 non-null object
    dtypes: float64(4), object(1)
    memory usage: 5.9+ KB





    array(['setosa', 'versicolor', 'virginica'], dtype=object)



* \# of Data points: 150
* Data types: 1st 4 columns are floats, last is object
* Column names:
    * Sepal.Length
    * Sepal.Width
    * Petal.Length
    * Petal.Width
    * Species
* Species of Flowers:
    * Setosa, Versicolor, Virginica 


##### 2.3
The data that I uploaded to my website, which you have downloaded, is based
on the data initially uploaded to the UC Irvine machine learning repository. It is
now known that this data contains errors in two of its rows (see the documentation
at https://archive.ics.uci.edu/ml/datasets/Iris). Using 1-indexing, these
errors are in the 35th and 38th rows. The 35th row should read 4.9,3.1,1.5,0.2,”Iris-setosa”,
where the fourth feature is incorrect as it appears in the file, and the 38th
row should read 4.9,3.6,1.4,0.1,”Iris-setosa”, where the second and third features are
incorrect as they appear in the file. Correct these entries of your DataFrame


```python
# Change error in 34th Row
iris.iloc[34, iris.columns.get_loc('Petal.Width')] = 0.2

#Change errors in 37th Row
iris.iloc[37, iris.columns.get_loc('Sepal.Width')] = 2.6
iris.iloc[37, iris.columns.get_loc('Petal.Width')] = 1.4
```

##### 3.3
The iris dataset is commonly used in machine learning as a proving ground for
clustering and classification algorithms. Some researchers have found it useful to
use two additional features, called *Petal ratio* and *Sepal ratio*, defined as the ratio
of the petal length to petal width and the ratio of the sepal length to sepal width,
respectively. Add two columns to you DataFrame corresponding to these two new
features. Name these columns Petal.Ratio and Sepal.Ratio, respectively.


```python
## Create two new columns for petal.ratio and sepal.ratio
iris['Petal.Ratio'] = iris['Petal.Length']/iris['Petal.Width']
iris['Sepal.Ratio'] = iris['Sepal.Length']/iris['Sepal.Width']
iris.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sepal.Length</th>
      <th>Sepal.Width</th>
      <th>Petal.Length</th>
      <th>Petal.Width</th>
      <th>Species</th>
      <th>Petal.Ratio</th>
      <th>Sepal.Ratio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
      <td>7.0</td>
      <td>1.457143</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
      <td>7.0</td>
      <td>1.633333</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>setosa</td>
      <td>6.5</td>
      <td>1.468750</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>setosa</td>
      <td>7.5</td>
      <td>1.483871</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
      <td>7.0</td>
      <td>1.388889</td>
    </tr>
  </tbody>
</table>
</div>



##### 2.4
Save your corrected and extended iris DataFrame to a csv file called iris_corrected.csv.
Please include this file in your submission


```python
## Save to csv file
iris.to_csv('iris_corrected.csv', index = False)
## Index name however seems to be created as a new unnamed column??
## How to make that not be the case? 
iris2 = pd.read_csv('iris_corrected.csv')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sepal.Length</th>
      <th>Sepal.Width</th>
      <th>Petal.Length</th>
      <th>Petal.Width</th>
      <th>Species</th>
      <th>Petal.Ratio</th>
      <th>Sepal.Ratio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
      <td>7.0</td>
      <td>1.457143</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
      <td>7.0</td>
      <td>1.633333</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>setosa</td>
      <td>6.5</td>
      <td>1.468750</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>setosa</td>
      <td>7.5</td>
      <td>1.483871</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
      <td>7.0</td>
      <td>1.388889</td>
    </tr>
  </tbody>
</table>
</div>



##### 2.5
Use a pandas aggregate operation to determine the mean, median, minimum, maximum
and standard deviation of the petal and sepal ratio for each of the three species
in the data set.


```python
iris.groupby('Species')['Petal.Ratio','Sepal.Ratio'].agg(['mean',
                                                         'median',
                                                         'min',
                                                         'max',
                                                         'std'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="5" halign="left">Petal.Ratio</th>
      <th colspan="5" halign="left">Sepal.Ratio</th>
    </tr>
    <tr>
      <th></th>
      <th>mean</th>
      <th>median</th>
      <th>min</th>
      <th>max</th>
      <th>std</th>
      <th>mean</th>
      <th>median</th>
      <th>min</th>
      <th>max</th>
      <th>std</th>
    </tr>
    <tr>
      <th>Species</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>setosa</th>
      <td>6.649429</td>
      <td>7.000000</td>
      <td>1.071429</td>
      <td>15.0</td>
      <td>2.783695</td>
      <td>1.480658</td>
      <td>1.467708</td>
      <td>1.268293</td>
      <td>1.956522</td>
      <td>0.131346</td>
    </tr>
    <tr>
      <th>versicolor</th>
      <td>3.242837</td>
      <td>3.240385</td>
      <td>2.666667</td>
      <td>4.1</td>
      <td>0.312456</td>
      <td>2.160402</td>
      <td>2.161290</td>
      <td>1.764706</td>
      <td>2.818182</td>
      <td>0.228658</td>
    </tr>
    <tr>
      <th>virginica</th>
      <td>2.780662</td>
      <td>2.666667</td>
      <td>2.125000</td>
      <td>4.0</td>
      <td>0.407367</td>
      <td>2.230453</td>
      <td>2.169540</td>
      <td>1.823529</td>
      <td>2.961538</td>
      <td>0.246992</td>
    </tr>
  </tbody>
</table>
</div>



#### 3. Plotting pandas DataFrames

##### 3.1
Use the built-in pandas plotting tools to make a box-and-whisker plot showing the
distribution of petal ratio and sepal ratio for each of the three species. Your plot
should have two subplots, one for petal ratio and one for sepal ratio. You may choose
the details of your plots (i.e., how to handle outliers, displaying mean vs median,
etc) however you think is best. Please include labels on your x- and y-axes and give
an appropriate title to your plot.


```python
#iris = iris.set_index('Species')

#Set up subplots and figure sizes
fig, axes = plt.subplots(nrows = 1, ncols=2, figsize = (20,10))

#plot Petal Ratio
a = iris.boxplot(column = ['Petal.Ratio'],by = ['Species'],
            ax = axes[0])

#plot Sepal Ratio
b = iris.boxplot(column = ['Sepal.Ratio'],by = ['Species'],
            ax = axes[1])

##Set y labels
a.set_ylabel('Petal Length to Petal Width Ratio')
b.set_ylabel('Sepal Length to Sepal Width Ratio')

#Set title
fig.suptitle('Boxplots of Petal and Sepal Ratios by Species')

_ = plt.show
```


![png](testm_files/testm_22_0.png)


##### 3.2
Use the built-in pandas plotting tools to make a scatter matrix plot for the four original
features (petal width, petal length, sepal width and sepal length). Each point in
the scatter plot should be colored according to its species. See the documentation
at https://pandas.pydata.org/pandas-docs/stable/visualization.html#
scatter-matrix-plot to get started.


```python
#Import scatter matrix
from pandas.plotting import scatter_matrix
```


```python
## Change type in iris to category
iris['Species'] = iris['Species'].astype('category')

## put species into classification coes (0,1,2) to plot
iris['Species_code'] = iris['Species'].cat.codes
```




    array([0, 1, 2])




```python
## Select just first 5 columns
iris_og = iris.iloc[:,0:5]

##Set colors for classification
colors_palette = {0: "red", 1: "green", 2: "blue"}
## Color by species code
colors = [colors_palette[c] for c in iris['Species_code']] 

##plot with scatter matrix
sm = scatter_matrix(iris_og, color = colors, diagonal = 'kde',
              figsize = (6,6))
    
#Show it, marvel at how pretty it is. Just look at those colors.
#Magnificent
_ = plt.show()
```


![png](testm_files/testm_26_0.png)

