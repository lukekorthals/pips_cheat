__version__ = 'dev'

def cheat(exercise_number: str):
    solutions = {  # Solutions are stored in a dictionary with the question number as key
        "Q3.2P.1": "1. make sure you have seaborn installed and loaded with import seaborn as sns \n2. import seaborn as sns, \n3. generate random uniform data with dat = np.random.uniform(-10, 10, 1000) \n4. create the boxplot with plt.boxplot(dat) \n5. create the violinplot with sns.violinplot(dat) \n6. add points to the violinplot with sns.stripplot(dat, color='white') \n7. save the plot with plt.savefig('random_violinplot.png') \n8. show the plot with plt.show()",
        "Q1.2P.1": "1. make sure you have numpy installed and loaded with import numpy as np \n2. create a numpy array another_array = np.zeros((2, 4, 6)) \n3. You can access the last element in this array with [-1] \n4. You can access the element of interest with element_of_interest = another_array[-1, 0, 2]",
        "Q2.2P.1": "1. make sure you have datetime installed and loaded with import datetime \n2. use datetime.datetime.now() to get the current datetime \n3. use .strftime('%H:%M') to get only the current hour and minute \n4. Now add some ifelse logic: if current_time >= '01:00' and current_time <= '04:00': print('Go to sleep!') elif current_time >= '08:00' and current_time <= '09:00':print('Eet je hagelslag!') else: print('Gut gemacht!')",
        "Q1.2P.4": "In the terminal code is executed line by line. When copying something and executing the line %paste, iPython knows to access the\nclipboard and execute the entire copied code from there. This is useful when copying code from a text editor or IDE and pasting it into the\nterminal.\n\nIn the IDE %paste does not work and it also doesnt make sense. As the script is executed all at once, the copied code can simply be pasted\nand there is no need to access the clipboard on runtime.\n\niPython is used to test things out, which is why relying on stored code in the clipboad is useful. Scripts are used to be executed again and again\nand it really doesnt make sense for it to access the clipboard in any way."
    }
    if exercise_number in solutions.keys():
        print(f"Solution for {exercise_number}:\n{solutions[exercise_number]}\n")
    else:  # if the question number is not in the dictionary, print a warning
        print(f"WARNING: No solution available for {exercise_number}. Please use one of the following: {solutions.keys()}")
