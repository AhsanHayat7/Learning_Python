#  Installation
*  Anaconda
*  vs code

# Reasons why we use conda commands
*  Conda commands help manage the complexity of dependencies and ensure a smooth and isolated development and deployment environment for your Python projects.
*  They provide a convenient way to create, manage, and share reproducible computing environments.

# Hello world
* windows -->Anaconda prompt -->python
```
print("Hello user welcome to the python world")
```
   * install python extension
   * click on run button
  
 # Make your own virtual environment 
 * Go to anaconda prompt and run these codes.The command is used to create a new virtual environment in Conda, a popular package and environment management system for Python.
``````
conda create -n
``````
```
conda create -n python12 python==3.12 -y
```
* Go to Vs code and make requirements.txt file and activate your environment.
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
* How we can change env into another enviroment by running this code.
  ```
  conda activate envname
  ```
* We can create env without python packages. And check virtual enviroment packages and libraries  by runnig this code.

```
conda create -n envname

conda create --name envname
```
```
conda list
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

* When we want to activate one env leaving the other by running this code.
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
* To get  the information of the env.
```
conda info
```
* We can create env in local repo.
```
conda create -p ./envname
```
* We can activate the local repo env.
```
activate Pathenv
```
* We can remove env from the local repo.
```
conda deactivate
```
```
conda env remove -p "envpath"
```
* We can also remove python packages version and libraries in environment by.
```
conda remove python
```
* Change directory to get into the parent folder we run.
```
cd..
```
* Info of folders.
```
dir
```
* We can ge into the folder by this code and press tab to get foldername.
```
cd foldername
```
* To get info of the folder we run.
```
dir/a
```
* To open vs code directly from the prompt.
  ```
  code .
  ```

