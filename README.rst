
Goal
-------
Him to integrate ableton link to smode using pybind to access cpp mapped function from python.
This repo is a fork of `aalink <https://github.com/artfwo/aalink>`_ for python 3.7.5 (aalink is a bit wonky under python 3.8)

Test
-------
I've try to recreate the `linkHut <https://github.com/Ableton/link/blob/master/examples/linkhut/main.cpp>`_ as a poc in exemple folder (the play/pause/stop doesn't sync for me on the official one so i need to take a look at this one later)
You can folow the `test plan <https://github.com/Ableton/link/blob/master/TEST-PLAN.md>`_ but using linkHut.py

Compile
-------
```
mkdir build
cd build
cmake ..
cmake --build .
```

License
-------
You can find the full text of the GPL license in the ``LICENSE`` file included
in this repository.

this code includes pybind11 and Ableton Link.

`pybind11 <https://pybind11.readthedocs.io/>`_

Copyright (c) 2016 Wenzel Jakob <wenzel.jakob@epfl.ch>, All rights reserved.

`pybind11 license <https://github.com/pybind/pybind11/blob/master/LICENSE>`_

`Ableton Link <https://ableton.github.io/link/>`_

Copyright 2016, Ableton AG, Berlin. All rights reserved.

`Ableton Link license <https://github.com/Ableton/link/blob/master/LICENSE.md>`_
