# Data Science and Toolkits

### Milestone 5

Repository of Bud

Task:
*Share your experience with the migration from a Linux OS to Windows OS.*

I separated this milestone into several sub-categories. Since we mostly worked with the
Linux Terminal, which is not available for Windows, I will list my substitutes for the
following Software packages:

1. Branching/Version control
2. Python
3. Container
4. PostgreSQL
5. Weights and Bias
6. Jupyter notebook

### 1.

The main difference for code version control and branching between the two operating systems
is that windows does not provide an all-inclusive terminal, where additional software such as **Git** can be installed. However, there are several alternatives which are useful for this task. Some resemble the Linux terminal more closely regarding its interactions, where as others are quite different regarding their "feel".

**Option 1:**

**Github Desktop** is a Windows app provided by the creators of the website. It provides all features a branching/version control tool needs. Further, it provides a graphical user interface (GUI), but does not allow to use git syntax. This can be an advantage or disadvantage, depending on the user and his/her preferences. Coming from the Linux terminal, I found it somewhat confusing at times what exactly I have to do instead of just the usual git syntax routine. Nevertheless, it is a viable alternative.

**Option 2:**

**Git Bash for Windows** has the most similarities to the Linux terminal and its built-in git. The app recognizes the same syntax as in the Linux terminal (since it is just the git version for Windows). I found this alternative most suitable for me, since I am quite familiar with git on Linux. However, Git Bash can only be used for version control. There is no built-in Python as is the case for the Linux Terminal. I am not sure how the interaction between Windows Git Bash and Docker or PostgreSQL is.


**Option 3:**

A third and interesting option is **SmartGit**. SmartGit is more similar to Github Desktop than Git Bash. It has a GUI and even some nice additions, such as a graphical representation of the different branches. This can be useful in some circumstances, especially when communication is lacking between the parties working on a project. However, the GUI can be confusing at times, especially in the beginning since it offers to many options, which you might never need. Further, a professional version is not free of charge.

**Option 4:**

Last but not least, the **Github** website can be used to version code. However, it is the least favorable option of all in my opinion since I am not completely certain that all features and commands are available. For example, I am not aware if it is possible to clone a repository from the website directly. However, uploading files and creating new branches is easy, but requires constant manual updates on your systems side and is thus the least favorable option of all, in my opinion.


*Helpful Websites for this task:*

https://desktop.github.com/

https://gitforwindows.org/

https://www.syntevo.com/smartgit/

https://github.com/

### 2.

I opted to use **Anaconda Spyder** as a substitute for the Linux integrated Python. The reasoning behind that is, that I am familiar with it and it solves the necessities outlined in this lecture. We mostly have to run the provided code and make some changes to it. All necessary modules
(such as **Keras**, **TensorFlow**, **Numpy**, **Pandas**, **Scikitlearn**, etc.)
can be downloaded in Anaconda. The main advantage of Anaconda is also its main disadvantage,
since it already comes with many Python modules pre-installed. Some of it is thus bloatware, which will be most likely never used. Nevertheless, coding and debugging came more natural to me in Spyder than in the built-in version of python in the terminal. This came more natural to me probably due to the familiarity I have gained with Spyder already but I always thought the built-in Python in the Linux Terminal and my interactions with it to be somewhat off-putting.

An alternative to Spyder would the vanilla version of Python 3 since it has less bloatware and might thus perform better/faster than Spyder and has additionally a higher degree of customizability. However, since I have not run into trouble with Spyder so far, I stick to it.


*Helpful Websites for this task:*

https://www.anaconda.com/

https://www.python.org/downloads/

### 3.

To dockerize code, the most suitable app is the **Docker Desktop for Windows** version. This windows app, as most of them, come with a GUI, which shows you each running container. Container management is also possible with it. It supports Linux containers as well as Windows containers and in the app you can individually adjust the resources available to Docker (such as CPU and memory space). Thus, this app should do the job for the tasks we were given throughout this lecture. The advantages and disadvantages are similar to the outlined apps which possess a GUI above.



*Helpful Websites for this task:*

https://docs.docker.com/docker-for-windows/

https://hub.docker.com/editions/community/docker-ce-desktop-windows/

### 4.

Regarding Relational Database management system (RDBMS), we worked with **PostgreSQL** throughout the lecture, which can be directly accessed by the Linux Terminal. To set up a PostgreSQL database on Windows, downloading and installing a server is a prerequisite. It is a possibility to use the Windows command prompt to interact with the database and thus has similar interactions as in the Linux Terminal. The differences regarding the syntax to set up and run PostgreSQL servers should thus be not fundamentally different between the two OS. Windows further allows to interact with a GUI, in case the command prompt is not preferred by the user. To connect Python (or in my case Spyder) to a PostgreSQL server, we have to import pyscopg in Python via (after downloading it from PyPI):

```sh
import psycopg2
```
After that, we can establish a connection as such:

```sh
connection = psycopg2.connect(user="...",                                   
password="...",                                   
host="...",                                   
port="...",                                   
database="...")
cursor = connection.cursor() cursor.execute("SELECT * FROM my_data")
```

This should do the trick and the tasks we were given during the lectures should be doable with this setup.

*Helpful Websites for this task:*

https://www.microfocus.com/documentation/idol/IDOL_12_0/MediaServer/Guides/html/English/Content/Getting_Started/Configure/_TRN_Set_up_PostgreSQL.htm

https://www.postgresql.org/

https://www.psycopg.org/docs/

https://pypi.org/project/psycopg2-binary/


### 5.

The usage of **Weights and Biases** should not be any different from the Linux OS since the access is established via Python/Spyder.  


*Helpful Websites for this task:*

https://www.wandb.ai


### 6.

The only difference for using **Jupyter Notebook** between Linux and Windows OS is its installation. When using Anaconda, it is possible to install the module directly via:

```sh
conda install -c conda-forge notebook
```

After the installation, we can run the notebook via (in the Windows prompt):

```sh
jupyter notebook
```

Further usage should not be any different than what we did on Linux throughout the lecture.


*Helpful Websites for this task:*

https://jupyter.org/install

https://jupyter.readthedocs.io/en/latest/running.html#running


### Concluding Remarks

Windows does not provide a one stop shop solution for the above mentioned tools as the Linux OS does.
There is no terminal, such as is the case on Linux, where you can do the version
control/branching, read and execute code, dockerize your applications, access a
server database or online applications. This means that one has to use several separate
applications in conjunction to achieve similar results. This can lead to convolution, but the
entry barrier may be lower for people who are used to GUIs and do not have a grasp
on the necessary syntax used in terminals so far. Further, it does not allow for trial
and error in a save "space" such as a virtual machine, unless you set up one with Windows
on it. However, this requires downloading all the above mentioned software, which might
significantly slow down the virtualbox, since some of them might have bloatware. I can see why we chose to opt for Linux throughout the lecture since the handling of all the data science tools and architecture is much more fluent on Linux. Further, the management of all the different applications on Windows significantly slows down the work flow. Switching from app to app can become cumbersome and interacting with GUIs slows down the work flow even further, especially when you know what you are doing. That being said, it might be easier for newcomers to get a hold of work flow, and the different apps might provide some clearer distinctions between the what the current focus/task is. This can result in less confusion in the beginning but can become slow when you exceed the beginner stage.
To conclude, a migration is definitely possible but requires some extra steps and software,
making Windows a sub-optimal choice for an all encompassing and clean solution for data scientists.
