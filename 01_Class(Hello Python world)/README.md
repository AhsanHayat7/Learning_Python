#  Installation
*  Anaconda
*  vs code

# Hello world
* windows -->Anaconda prompt -->python
```
print("Hello user welcome to the python world")
```
   * install python extension
   * click on run button
  
 # Make your own virtual environment 
 * Go to anaconda prompt and run these codes.
``````
conda create -n
``````
```
conda create -n python12 python==3.12 -y
```
* Go to Vs code and make requirements.txt file and write your packages.
```
conda activate python12
```
```
pip install -r requirements.txt
```
* Now your own virtual environment is formed you can use it by selecting the python12 in the Vs code .

* We can check how many virtaul environemt are created by runnig this code.

 ```
  conda env list
```
* How we can change into another enviroment by running this code.
  ```
  conda activate envname
  ```
* We can save and check enviroment without packages in the env by runnig this code.

```
conda create -n envname

conda create --name envname
```
```
coda list
```
* We can activate and deactivate base env by ruuning this code.
```
activate
```
```
conda activate
```
```
deactivate
```

* When we want to activate any env by running this code.
```
  conda activate envname
```
* We can updated the conda version by running this code.
```
conda update conda
```
* We can install python in the env by runnig this code.
```
conda install python=version
```
  
