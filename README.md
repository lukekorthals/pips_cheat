# pips_cheat
Published as part of coursework for the 3rd week assignment of the programming in psychological science course.

Contains one function cheat() that can be used to get the solutions for assignment questions.
Currently supports the following questions:
- "Q1.2P.1"
- "Q1.2P.4"
- "Q2.2P.1"
- "Q3.2P.1"

# Installation
```python
pip install git+https://github.com/lukekorthals/pips_cheat
``` 

# How to use
Call the function with a supported question ID (e.g., "Q3.2P.1") and you will receive the correct solution. 


```python

```


```python
from pips_cheat import cheat
cheat("Q3.2P.1")
```

    Solution for Q3.2P.1:
    1. make sure you have seaborn installed and loaded with import seaborn as sns 
    2. import seaborn as sns, 
    3. generate random uniform data with dat = np.random.uniform(-10, 10, 1000) 
    4. create the boxplot with plt.boxplot(dat) 
    5. create the violinplot with sns.violinplot(dat) 
    6. add points to the violinplot with sns.stripplot(dat, color='white') 
    7. save the plot with plt.savefig('random_violinplot.png') 
    8. show the plot with plt.show()
    
    
