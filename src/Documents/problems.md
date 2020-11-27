## Encountered Problems Outside of Milestones

#### 1.
The virtualbox on Microsoft Surface kept crashing, which led me to switch computers. When the Virtualbox crahsed,
I was no able to save the status quo (if I do, the virtualbox launches into the crashed mode).

#### 2.
New computer had SVM disabled and changes in the BIOS (I have an MSCI motherboard and AMD CPU) had to be made to enable it.

#### 3.
When running:

```sh
sudo apt-get install python3-pip
```
the following message shows:\
"
Package python3-pip is not available, but is referred to by another package.
This may mean that the package is missing, has been obsoleted, or is only available from another source.\
E: Package 'python3-pip' has no installation candidate.
"

This is confirmed when running:

```sh
apt list --upgradable
```
Since the python3-pip module is not listed.

However, it is possible to install pip by downloading it directly from: https://bootstrap.pypa.io/get-pip.py
with the following commands:

```sh
sudo apt install curl
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```
However, when running the last command the following message shows:

" ModuleNotFoundError: No module named 'distutils.util'"

To solve this, I ran:

```sh
sudo apt-get install python3-distutils
sudo apt-get install python3-apt
```
While the last command checks if the used Python version is up-to-date.

Then I try to install pip again with:

```sh
python3 get-pip.py
```

This leads to the following message:

"
WARNING: Scripts pip, pip3 and pip3.8 are installed in 'home/ubuntu/.local/bin' which is not on PATH"

To fix this, I ran:
```sh
export PATH=/home/ubuntu/.local/bin:$PATH
```

To check if this worked I ran:

```sh
pip install -U pip
```

which gave me no WARNING message.

#### 4.
Updating ubuntu 20.04 via:

```sh
sudo apt-get update
```
and

```sh
sudo apt-get upgrade
```

led me to increase disk space since it stopped due to an error message that not enough disk space was available. However, I refrain from updating the virtualbox from now on since it increases the likelihood that the virtualbox crashes.

#### 5.
When the virtualbox crashes again (for reasons unknown until now), I start back at 1. and rerun these commands to get the virtualbox up and running for the project. Also, all packages (TensorFlow, matplotlib, keras, etc.) needed for the project have to be reinstalled.


This file also serves the purpose as a recovery tool when the virtualbox crashes again.
