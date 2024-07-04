
Goal
-------
Aims to integrate ableton link to smode using pybind to access cpp mapped function from python.
This repo is a fork of [aalink](https://github.com/artfwo/aalink) for python 3.7.5 (aalink is a bit wonky under python 3.8)

Test
-------
I've try to recreate the [linkHut](https://github.com/Ableton/link/blob/master/examples/linkhut/main.cpp) as a poc in exemple folder (the play/pause/stop doesn't sync for me on the official one so i need to take a look at this one later)
You can folow the [test plan](https://github.com/Ableton/link/blob/master/TEST-PLAN.md)  but using linkHut.py

Compile
-------
```
mkdir build
cd build
cmake ..
cmake --build . --config Release
```
then you can copy `smodeLink.cp37-win_amd64.pyd` into smode python directory
```
# Now you can import your module as if it was installed in the standard library
import smodeLink
```
