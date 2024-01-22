#  Installation
*  Anaconda
*  vs code
*  
# Reasons to Use Conda Commands in Python

## 1. Environment Isolation
- Conda allows you to create isolated environments for different projects, avoiding conflicts between dependencies.

## 2. Dependency Management
- Simplifies the process of installing and managing dependencies, ensuring consistent environments.

## 3. Cross-Platform Compatibility
- Works seamlessly on Windows, macOS, and Linux, making it easy to share and reproduce environments.

## 4. Package Installation and Updates
- Easily install packages from repositories and update them to newer versions.

## 5. Ease of Use
- Conda commands are straightforward, making it easy to create, activate, and deactivate environments, as well as manage packages.

## 6. Reproducibility
- Environments can be exported to YAML files, facilitating the recreation of the same environment on other machines.

## 7. Virtual Environments Without Python
- Not limited to managing Python packages; also supports packages for other programming languages.

## 8. Package Channels
- Supports channels, providing access to a wide range of libraries and versions beyond the default channels.

## 9. Community and Open Source
- Conda is an open-source project with an active community, ensuring support and resources are readily available.

## 10. Integration with Data Science and Scientific Computing
- Widely used in data science and scientific computing environments, simplifying the installation of commonly used libraries.

In summary, Conda commands are valuable for managing Python environments and packages due to their simplicity, cross-platform compatibility, and effective handling of dependencies. They are particularly popular in fields such as data science and scientific computing where reproducibility and package management are crucial.


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
* We can ge into the folder by running this code and press tab to get foldername or paste the path of the folder.
```
cd foldername
cd path_of_folder
```
* To get info of the folder we run.
```
dir/a
```
* To open vs code directly from the prompt.
  ```
  code .
  ```

